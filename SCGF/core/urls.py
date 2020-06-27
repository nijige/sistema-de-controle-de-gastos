from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.group, name='group'),
    path('transaction/', views.newTransaction, name='add-transaction'),
    path('edit/<int:id>', views.editTransaction, name='edit-transaction'),
    path('delete/<int:id>', views.deleteTransaction, name='delete-transaction'),
    path('group/newgroup/', views.newGroup, name="new-group"),
    path('relatorio/', views.relatorio, name="relatorio"),
]