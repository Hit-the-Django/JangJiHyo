from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloBabyLion(request):
    return render(request, 'intro.html')