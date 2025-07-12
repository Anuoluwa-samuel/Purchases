from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the Index Page")

def staff(request):
    return HttpResponse("This is the staff Page")