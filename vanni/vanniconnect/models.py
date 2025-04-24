from django.db import models

# Create your models here.
from django.db import models

SEVERITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
]

class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, blank=True)

    def __str__(self):
        return f"{self.name} - {self.request_type}"


class VoiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    transcribed_text = models.TextField()
    severity = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"VoiceRequest from {self.name} - {self.severity}"
