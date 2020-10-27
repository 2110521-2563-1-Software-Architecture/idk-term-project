from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, RegisterViewSet, SigninViewSet

router = DefaultRouter()
router.register(r'link', LinkViewSet, basename='link')
router.register(r'signup', RegisterViewSet, basename='signup')
router.register(r'signin', SigninViewSet, basename='signin')

urlpatterns = router.urls