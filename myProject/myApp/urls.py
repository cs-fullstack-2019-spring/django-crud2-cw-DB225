from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('contacts/edit/<int:ID>', views.editContact, name="edit"),
    path('contacts/delete/<int:ID>', views.delete, name="delete"),
]