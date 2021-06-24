from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('log_out/', views.log_out, name="logout"),
    path('posts/<int:post_id>/', views.posts, name="posts"),
]