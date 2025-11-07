from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact


@login_required
def contacts(request, *args, **kwargs):
    user = request.user
    qs = Contact.objects.filter(user=user)

    # Debug: Print total contacts vs filtered contacts
    # total_contacts = Contact.objects.count()
    # print(f"Current user: {user}")
    # print(f"Total contacts in DB: {total_contacts}")
    # print(f"Contacts for {user}: {qs.count()}")
    # print(f"Query: {qs.query}")

    context = {"object_list": qs}

    return render(request, "contacts/contacts_list.html", context)
