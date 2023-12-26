from django.shortcuts import render,HttpResponse
from .models import Posts
# Create your views here.

def home(request):
    items=Posts.objects.all()

    return render(request,"home.html",{"items":items})
def deliver(request,name):
    items=Posts.objects.all()
    for i in items:
        if i.title == name:
            return render(request,"blog.html",{"i":i})

    
