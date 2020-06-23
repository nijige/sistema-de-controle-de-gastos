from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.group, name='group'),
    path('transaction/', views.newTransaction),
]