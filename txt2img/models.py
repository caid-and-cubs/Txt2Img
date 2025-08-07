from django.db import models
import uuid
import os


def image_upload_path(instance, filename):
    """Generate upload path for generated images"""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('generated_images', filename)


class GeneratedImage(models.Model):
    """Model to store generated images"""
    prompt = models.TextField(help_text="Text prompt used to generate the image")
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    generation_time = models.FloatField(null=True, blank=True, help_text="Time taken to generate in seconds")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Image generated at {self.created_at} for prompt: {self.prompt[:50]}..."
