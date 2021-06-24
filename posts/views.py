from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {
        "user": request.user,
        "post": post,
        "comments": post.comments.all(), #"""post.comments.all"""
    })
