from django.db import models

# Create your models here.


class Event(models.Model):
    class EventType(models.TextChoices):
        VIEWED = "viewed", "View Event"
        CREATED = "created", "Create Event"

    event_type = models.CharField(
        max_length=50, default=EventType.VIEWED, choices=EventType.choices
    )
    object_id = models.IntegerField(blank=True, default=-1)
    model_name = models.CharField(max_length=200, default="contacts.content")
    timestamp = models.DateTimeField(auto_now_add=True)
