import math
import random

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Word, Chapter


# Create your views here.

def index(request):
    array = Word.objects.all()

    for w in array:
        w.word_to_string()
        w.save()

    dict = {}
    for word in array:
        dict[word.chapter.__str__()] = word

    return render_to_response('words/index.html', {'dictionary': array, 'chapters':Chapter.objects.all()})

def word_view(request, id):
    w = Word.objects.get(pk = id)
    return render_to_response('words/word_view.html', {'word' : w})

def chapter(request, chapter_id):
    c = Chapter.objects.get(pk = chapter_id)
    return render_to_response('words/chapter_view.html', {'chapter': c})

def quiz(request):
    array = Word.objects.all()
    rand = random.sample(list(array), 1);
    o = rand[0]
    return render_to_response('words/quiz.html', {'word' : o})

def answer(request):
    return HttpResponse('sprawdzanie odpowiedzi')

def exercise(request):
    array = Word.objects.all()
    return render_to_response('words/exercise.html', {'words':array})
