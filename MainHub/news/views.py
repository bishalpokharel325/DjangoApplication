from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, "frontend/pages/home.html")

# Create your views here.
def about(request):
    data = {'articleData': Article.objects.all()}
    return render(request, "frontend/pages/about.html", data)
def contact(request):
    return render(request,"frontend/pages/contact.html")
def register(request):
    return render(request,"frontend/pages/register.html")
def login(request):
    return render(request,"frontend/pages/login.html")
