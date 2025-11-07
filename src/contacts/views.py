from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact


@login_required
def contacts(request, *args, **kwargs):
    # user = request.user
    qs = Contact.objects.all()

    context = {"object_list": qs}

    return render(request, "contacts/contacts_list.html", context)
