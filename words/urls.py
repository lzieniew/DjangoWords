from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^word/(?P<id>[0-9]+)/$', views.word_view, name = 'word_view'),
    url(r'^quiz/$', views.quiz, name = 'quiz'),
    url(r'^quiz/answer/$', views.answer, name="answer"),
    url(r'^exercise/$', views.exercise, name='exercise'),
    url(r'^chapter/(?P<chapter_id>[0-9]+)/$', views.chapter, name = 'chapter_view'),
    url(r'^dupa/$', views.test_view, name='test')
]