from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'link', LinkViewSet, basename='link')
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = router.urls