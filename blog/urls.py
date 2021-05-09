from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('create/', views.create_user, name="new_user"),
    path('posts/<int:post_id>/', views.posts, name="posts"),
    path('log_out/', views.log_out, name="logout")
]