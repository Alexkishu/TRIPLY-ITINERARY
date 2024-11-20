from django.db import models

# Create your models here.
from django.db import models

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

# models.py
from django.db import models

class Itinerary(models.Model):
    destination = models.CharField(max_length=255)
    user_email = models.EmailField()
    # other fields...

    def __str__(self):
        return self.destination
