from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request, "RolCCApp/home.html")

def levelup(request):

    return render(request, "RolCCApp/levelup.html")

def search(request):

    return render(request, "RolCCApp/search.html")

def news(request):

    return render(request, "RolCCApp/news.html")
