from django.urls import path
from .views import MediaView
from rest_framework import routers



router = routers.SimpleRouter()
router.register(r'media', MediaView)
urlpatterns = router.urls