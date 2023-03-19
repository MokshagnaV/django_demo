from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render("<h1>Hello World</h1>")