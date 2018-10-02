from django.conf.urls import url

from core.views import CropView

urlpatterns = [
    url(r'api/crop_image/$', CropView.as_view(), name="crop_image"),
]
