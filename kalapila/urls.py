from django.conf.urls import include, url
from django.contrib import admin
import os

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^admin/', admin.site.urls),
]
