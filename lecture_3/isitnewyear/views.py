from django.shortcuts import render
from datetime import date

def index(request):
    newyear = date.today().day == 1 and date.today().month == 1
    return render(request, "isitnewyear/index.html", {
        "newyear":newyear
    })