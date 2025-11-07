from django.urls import path
from . import views

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("contacts/<int:id>/", views.contact_detail, name="contact-detail"),
]
