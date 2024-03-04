from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':  'Ali',
        'title':   'Blog Post 1',
        'content': 'This is the first post here',
        'date_posted': 'Febuary 26, 2024'
    },
    {
        'author':  'James',
        'title':   'Blog Post 2',
        'content': 'This is the second post here',
        'date_posted': 'Febuary 28, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')