from django.http import HttpResponse
from random import randint
from django.shortcuts import render

def status(request):

    context = {
        "random_color": lambda: randint(0, 255),
    }
    return render(request, "tutorial_project/status.html", context)
