from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hi you are at home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("hi you are at about page")

def contact(request):
    return HttpResponse("hi you are at contact page")