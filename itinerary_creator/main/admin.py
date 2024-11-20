from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Itinerary

@admin.action(description='Send Itinerary Email')
def send_itinerary_email_action(modeladmin, request, queryset):
    for itinerary in queryset:
        send_mail(
            subject=f"Your {itinerary.destination.title()} Travel Itinerary",
            message=f"Hello! Here's your itinerary for {itinerary.destination}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[itinerary.user_email],
            fail_silently=False,
        )

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    actions = [send_itinerary_email_action]

