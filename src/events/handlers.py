from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event


@receiver(post_save)
def handle_post_save_signal(sender, instance, created, *args, **kwargs):
    if sender == Event:
        return  # Avoid handling Event model saves to prevent recursion

    elif isinstance(instance, Event):
        return  # Avoid handling Event instances
    event_type = Event.EventType.SAVE
    if created:
        event_type = Event.EventType.CREATED
    Event.objects.create(
        # user=instance.user,
        event_type=event_type,
        content_object=instance.content_object,
    )
