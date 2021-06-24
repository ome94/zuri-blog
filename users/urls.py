from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name="login"),
    path('new/', views.register, name="new_user"),
    path('create/', views.create_user, name="create_user"),
]