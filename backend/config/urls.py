from django.contrib import admin
from django.urls import path, include, re_path
from redirect.views import RedirectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import CustomJWTSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('signin/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer)),
    re_path(r'^(?!admin)([a-zA-Z0-9]){5}$', RedirectViewSet.redirect, name='redirect')
]
