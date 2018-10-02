from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(core_urls)),
]
