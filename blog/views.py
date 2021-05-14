from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        "title": "Home",
        "posts": Post.objects.all(),
        "user": request.user
    })

def posts(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {
        "post": post,
        "user": request.user
    })

def log_in(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return render(request, "login.html", {
                "message": "Login failed. Please try again with the correct credentials"
            })

        login(request, user)
        return HttpResponseRedirect(reverse('home'))

    elif request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))

        return render(request, 'login.html')

    else:
        return HttpResponseRedirect(reverse('home'))

    

def register(request):
    return render(request, 'register.html',)

def create_user(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    username = request.POST["username"]
    password = request.POST["password"]
    
    new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
    new_user.save()

    return render(request, 'success.html', {
        "message": f"You have been registered successfully{request.method}", 
    })

def log_out(request):
    logout(request  )
    return render(request, 'success.html', {
        "message": "You've been successfully logged out",
        "loggedin": request.user.is_authenticated
    })
