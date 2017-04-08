from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^word/P<id>[0-9]+/$', views.word_view, name = 'word_view')
]