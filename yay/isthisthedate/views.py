from django.shortcuts import render
from datetime import datetime
from django.http import Http404
def index(request):
    return render(request, "isthisthedate/index.html")

def checkdate(request, checkdate):
    try:
        dd = int(checkdate[:2])
        mm = int(checkdate[3:5])
        yyyy = int(checkdate[6:10])
    except ValueError:
        if_date = False
        return render(request, "isthisthedate/checkdate.html", {
        "if_date": if_date 
        }) 
    if dd == datetime.now().day and mm == datetime.now().month and yyyy == datetime.now().year :
        if_date = True
    else:
        if_date = False
    return render(request, "isthisthedate/checkdate.html", {
        "if_date": if_date 
        })