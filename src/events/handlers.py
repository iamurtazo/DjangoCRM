from django.dispatch import receiver
from .models import Event
from .signals import event_did_trigger


@receiver(event_did_trigger)
def handle_event_signal(sender, event_type, content_object, user=None, *args, **kwargs):
    event_object = Event.objects.create(
        event_type=event_type,
        content_object=content_object,
        user=user,
    )
    print(f"Event created: {event_object}")
