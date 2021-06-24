from django.contrib.auth import logout
from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        "title": "Home",
        "posts": Post.objects.all(), #"""[Main Story, [latest stories], [other posts]]"""
        "user": request.user
    })

def posts(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {
        "user": request.user,
        "post": post,
        "comments": post.comments.all(), #"""post.comments.all"""
    })

def log_out(request):
    logout(request  )
    return render(request, 'success.html', {
        "message": "You've been successfully logged out",
        "loggedin": request.user.is_authenticated
    })
