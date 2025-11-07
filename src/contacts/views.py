from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact
from django.http import Http404

from events.models import Event


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

    return render(request, "contacts/list.html", context)


@login_required
def contact_detail(request, id=None, *args, **kwargs):
    instance = Contact.objects.filter(id=id, user=request.user).first()

    if not instance:
        raise Http404(f"Contact with id {id} does not exist")

    context = {"object": instance}

    Event.objects.create(
        user=request.user,
        event_type=Event.EventType.VIEWED,
        content_object=instance,
    )

    return render(request, "contacts/detail.html", context)
