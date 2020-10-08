from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from django.utils.crypto import get_random_string

from .serializers import LinkSerializer
from linkurl.models import Link
from users.models import CustomUser

def generateLink() :
    sh = get_random_string(length=5)
    while Link.objects.filter(link_shorten=sh).exists() :
        sh = get_random_string(length=5)
    return sh

class LinkViewSet(viewsets.ModelViewSet) :
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def create(self, request, *args, **kwargs) :
        user_id = request.data['user_id']
        link_original = request.data['link_original']

        # Validate user_id
        if user_id and not CustomUser.objects.filter(user_id=user_id).exists() :
            return HttpResponseBadRequest('The user_id is invalid.')
        # Create new link
        link_shorten = generateLink()
        serializer = self.get_serializer(data={'link_shorten': link_shorten, 'link_original': link_original, 'link_user': user_id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response('idk.ly/' + link_shorten)