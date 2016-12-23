from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^hello/', 'myapp.views.hello', name = 'hello'),
]
