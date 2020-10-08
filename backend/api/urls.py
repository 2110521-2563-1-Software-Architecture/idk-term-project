from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet

router = DefaultRouter()
router.register(r'link', LinkViewSet, basename='link')

urlpatterns = router.urls