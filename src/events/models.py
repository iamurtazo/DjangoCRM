from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    class EventType(models.TextChoices):
        UNKNOWN = "unknown", "Unknown Event"
        VIEWED = "viewed", "View Event"
        CREATED = "created", "Create Event"
        SAVED = "save", "Save or Update Event"

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The user who triggered the event",
        related_name="myevents",
    )

    event_type = models.CharField(
        max_length=50, default=EventType.VIEWED, choices=EventType.choices
    )
    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    content_object = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
