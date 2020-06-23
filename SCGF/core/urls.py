from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('',views.login, name='/login'),
    path('group/', views.group, name='group'),
]