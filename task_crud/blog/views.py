from django.shortcuts import render
from .models import Post, Reader

# Create your views here.
def home(request):
    if "loggedin" not in request.session:
        request.session["loggedin"] = False

    return render(request, 'index.html', {
        "title": "Home",
        "posts": Post.objects.all(),
        "loggedin": request.session["loggedin"],
    })

def posts(request, post_id):
    post = Post.get('id')
    return render(request, 'post.html', {
        "post": post,
        "loggedin": request.session["loggedin"],
    })

def login(request):
    if request.method == "POST":
        # verify user
        # authenticate user
        user_name = request.POST["user_name"]
        form_password = request.POST["password"]
        user = Reader.objects.get(user_name=user_name)
        if  user.password != form_password:
            return render(request, "login.html", {
                "message": "Login failed. Please try again with the correct credentials"
            })

        # create a user session
        request.session["loggedin"] = True
        return render(request, 'index.html', {
            "loggedin": request.session["loggedin"]
        }) # render page with a session stored showing the users' name

    return render(request, 'login.html', {
        "title": "Login",
        "loggedin": request.session["loggedin"],
    })

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        # validate user input,
        # I ought to validate but due to shortage of time,
        # I'll trust the user to give a valid input,
        # The next time I have a go at this, it must be done.
        if Reader.object.get(user_name=user_name) is not None:
            # register new user
            new_user = Reader(first_name, last_name, user_name, password)
            new_user.save()

        return render(request, 'success.html', {
            "message": "You have been registered successfully",
        })

    return render(request, 'register.html', {
        "title": "Register",
        "loggedin": request.session["loggedin"],
    })

def logout(request):
    del request.session
    return render(request, 'success.html', {
        "message": "You've been successfully logged out",
        "loggedin": request.session["loggedin"]
    })
