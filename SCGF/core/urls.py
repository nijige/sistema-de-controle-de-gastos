from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.group, name='group'),
    path('login/',views.login)

]