from django.shortcuts import render

def index(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def news(request):
    return render(request,'news.html')

def contact(request):
    return render(request,'contact.html')


def destinations(request):
    return render(request,'destinations.html')


def elements(request):
    return render(request,'elements.html')
