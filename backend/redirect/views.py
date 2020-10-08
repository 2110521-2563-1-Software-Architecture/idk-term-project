from django.shortcuts import redirect
from rest_framework import viewsets
from django.http import HttpResponseNotFound
from linkurl.models import Link

class RedirectViewSet(viewsets.ModelViewSet) :
    def redirect(request, *args) :
        link_shorten = request.path.strip('/')
        try :
            link_original = Link.objects.get(link_shorten=link_shorten).link_original
        except Exception as e :
            return HttpResponseNotFound('The shorten link does not exist.')
        return redirect(link_original)