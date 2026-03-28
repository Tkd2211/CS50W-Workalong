from django.shortcuts import render

tasks = ["one","2"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":tasks
    })
