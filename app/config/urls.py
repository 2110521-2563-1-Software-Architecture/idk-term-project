from django.contrib import admin
from django.urls import path, include, re_path
from redirect.views import RedirectViewSet
from api.serializers import CustomJWTSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'^(?!admin)([a-zA-Z0-9]){5,12}$', RedirectViewSet.redirect, name='redirect')
]