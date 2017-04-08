from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Word


# Create your views here.

def index(request):
    array = Word.objects.all()
    return render_to_response('words/index.html', {'my_array': array})