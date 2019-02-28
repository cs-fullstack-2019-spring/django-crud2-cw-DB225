from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ContactModel
from .forms import ContactForm


# This page is for all the contacts
def index(request):
    addContact = ContactModel.objects.all()
    return render(request, 'myApp/index.html', {'addContact': addContact})


# This page is to add new users
def contacts(request):
    newContact = ContactForm(request.POST or None)
    if (newContact.is_valid()):
        newContact.save()
        return redirect('index')
    return render(request, 'myApp/contacts.html', {"newContact": newContact})


def editContact(request, ID):
    edit_contact = get_object_or_404(ContactModel, pk=ID)
    edit_form = ContactForm(request.POST or None, instance=edit_contact)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'myApp/contacts.html', {'edit_form': edit_form})


def delete(request,ID):
    deleted_contact = get_object_or_404(ContactModel, pk=ID)
    if request.method == 'POST':
        deleted_contact.delete()
        return redirect('index')

    return render(request,'myApp/delete.html', {"deleted_contact": deleted_contact})
