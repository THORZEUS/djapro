from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Posts

def index(request):

    posts = Posts.objects.all()#[:10]

    context = {

    'title':'Latest posts',
    'posts': posts

    }

    #return HttpResponse ("Hello Guapo")
    return render (request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {

    'post': post
    }
    return render(request,'posts/details.html', context)


