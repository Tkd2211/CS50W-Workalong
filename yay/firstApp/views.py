from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "firstApp/index.html")
def scale(request):
    return HttpResponse("scale is hot!")
def greet(request, name):
    return render(request, "firstApp/greet.html", {
        "name": name.capitalize()
        })