from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponseBadRequest
from django.utils.crypto import get_random_string
from django.db.models import Count

from .serializers import LinkSerializer, CustomUserSerializer
from linkurl.models import Link
from users.models import CustomUser
from access_log.models import AccessLog


def generateLink():
    sh = get_random_string(length=5)
    while Link.objects.filter(link_shorten=sh).exists():
        sh = get_random_string(length=5)
    return sh


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def retrieve(self, request, *args, **kwargs):
        uid = self.kwargs["pk"]
        if not CustomUser.objects.filter(user_id=uid).exists():
            return HttpResponseBadRequest("The user id is invalid.")
        bs = Link.objects.filter(link_user=uid)
        serializer = LinkSerializer(bs, many=True)
        for i in serializer.data:
            i["link_access"] = len(
                AccessLog.objects.filter(access_log_shorten_url=i["link_shorten"])
            )
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_id = request.data["user_id"]
        link_original = request.data["link_original"]

        # Validate user_id
        if user_id and not CustomUser.objects.filter(user_id=user_id).exists():
            return HttpResponseBadRequest("The user id is invalid.")
        # Create new link
        link_shorten = generateLink()
        serializer = self.get_serializer(
            data={
                "link_shorten": link_shorten,
                "link_original": link_original,
                "link_user": user_id,
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(link_shorten)


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        user_name = request.data['user_name']
        try:
            CustomUserSerializer.create(CustomUserSerializer(), validated_data=request.data)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
        return Response('User: ' + user_name + ". Registration successful!")