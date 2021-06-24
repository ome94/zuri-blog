from django.contrib.auth import logout
from django.shortcuts import render
from posts.models import Post

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        "title": "Home",
        "posts": Post.objects.all(), #"""[Main Story, [latest stories], [other posts]]"""
        "user": request.user
    })

def log_out(request):
    logout(request  )
    return render(request, 'success.html', {
        "message": "You've been successfully logged out",
        "loggedin": request.user.is_authenticated
    })
