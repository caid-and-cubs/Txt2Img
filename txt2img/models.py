# models.py
from django.db import models
from django.utils import timezone

class GeneratedImage(models.Model):
    prompt = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    generation_time = models.FloatField(null=True, blank=True)  # seconds
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Image: {self.prompt[:50]}..." if len(self.prompt) > 50 else self.prompt

class APIUsage(models.Model):
    endpoint = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    response_time = models.FloatField(null=True, blank=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.endpoint} - {self.timestamp}"

# Create your models here.
