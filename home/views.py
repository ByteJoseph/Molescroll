from django.shortcuts import render,HttpResponse
from .models import Posts
# Create your views here.

def home(request):
    items=Posts.objects.all()

    return render(request,"home.html",{"items":items})
