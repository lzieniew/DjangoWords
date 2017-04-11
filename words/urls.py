from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<id>[0-9]+)/word/$', views.word_view, name = 'word_view'),
    url(r'^quiz/$', views.quiz, name = 'quiz'),
    url(r'^quiz/answer/$', views.answer, name="answer")
    url(r'^exercise/&', views.exercise, name='exercise')
]