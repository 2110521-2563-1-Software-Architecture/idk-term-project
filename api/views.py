from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.http import HttpResponseBadRequest
from django.utils.crypto import get_random_string
from django.db.models import Count
from django.db.models.functions import TruncDate

from .serializers import LinkSerializer, CustomUserSerializer, CustomJWTSerializer
from linkurl.models import Link
from users.models import CustomUser
from access_log.models import AccessLog
from access_log.serializers import AccessLogSerializer

import re
from datetime import *

def generateLink():
    sh = get_random_string(length=5)
    while Link.objects.filter(link_shorten=sh).exists():
        sh = get_random_string(length=5)
    return sh

def validateLink(url):
    if not url.startswith(("http://", "https://", "ftp://", "ftps://")):
        url = "http://" + url
    regex = re.compile(
        r'^(?:http|ftp)s?://' #http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain
        r'localhost|' #localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' #ip
        r'(?::\d+)?' #port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url) is not None:
        return url, 1
    else: return url, 0


class LinkViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def list(self, request):
        uid = request.user
        if not CustomUser.objects.filter(user_name=uid).exists():
            return Response("The user token is invalid.", status=401)
        bs = Link.objects.filter(link_user=uid)
        serializer = LinkSerializer(bs, many=True)
        accesslog_count = (
            AccessLog.objects.filter(access_log_shorten_url__link_user=uid)
                .values('access_log_shorten_url')
                .annotate(total=Count('access_log_shorten_url'))
        )
        accesslog_count = {i["access_log_shorten_url"]:i["total"] for i in accesslog_count}
        for i in serializer.data:
            try:
                i["link_access"] = accesslog_count[i["link_shorten"]]
            except KeyError:
                i["link_access"] = 0
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        link_original, flag = validateLink(request.data["link_original"])
        if flag == 0: return HttpResponseBadRequest("The URL is invalid.")

        # Switch between registered and anonymous users
        if request.user.is_authenticated:
            user_id = request.user.user_id
        else:
            user_id = None
    
        # Validate user_id
        if user_id and not CustomUser.objects.filter(user_id=user_id).exists():
            return HttpResponseBadRequest("The user token not found.")
        # Create new link
        link_shorten = request.data['link_shorten'] if request.data['link_shorten'] else generateLink()
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

    def destroy(self, request, *args, **kwargs):
        uid = request.user
        instance = self.get_object()
        if instance.link_user != uid: return Response("This user does not own this link!", status=401)
        self.perform_destroy(instance)
        return Response("Deleted.", status=204)


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


class SigninViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = CustomJWTSerializer

    def create(self, request, *args, **kwargs):
        try:
            token = CustomJWTSerializer.validate(CustomJWTSerializer(), attrs=request.data)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
        return Response(token)


class AccessLogViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AccessLogSerializer

    def list(self, request):
        uid = request.user
        if not CustomUser.objects.filter(user_name=uid).exists():
            return Response("The user token is invalid.", status=401)
        accesslog =(
            AccessLog.objects.annotate(access_date=TruncDate("access_log_access_datetime"))
            .filter(access_log_shorten_url__link_user=uid)
            .values("access_log_shorten_url","access_date")
            .annotate(access_count=Count("access_log_shorten_url"))
        )
        access_data = dict()
        for i in accesslog:
            try:
                access_data[i["access_log_shorten_url"]][i["access_date"]] = i["access_count"]
            except KeyError:
                access_data[i["access_log_shorten_url"]] = dict()
                access_data[i["access_log_shorten_url"]][i["access_date"]] = i["access_count"]

        out = list()
        bs = Link.objects.filter(link_user=uid)
        for i in bs:
            shorten_url = i.link_shorten
            tmp = dict()
            tmp["access_log_shorten_url"] = shorten_url
            tmp["access_data"] = list()
            access_date = date.today()-timedelta(days=29)
            for j in range(30):
                if shorten_url in access_data:
                    if access_date in access_data[shorten_url]:
                        tmp["access_data"].append({"access_date":access_date,"access_count":access_data[shorten_url][access_date]})
                    else:
                        tmp["access_data"].append({"access_date":access_date,"access_count":0})
                else:
                    tmp["access_data"].append({"access_date":access_date,"access_count":0})
                access_date += timedelta(days=1)
            out.append(tmp)
        return Response(out)
