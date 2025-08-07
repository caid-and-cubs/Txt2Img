from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.base import ContentFile
from django.conf import settings
import json
import logging
import uuid
import io
from .models import GeneratedImage
from .services import stable_diffusion_service

logger = logging.getLogger(__name__)


def home(request):
    """Render the main application page"""
    recent_images = GeneratedImage.objects.all()[:6]  # Get 6 most recent images
    context = {
        'recent_images': recent_images
    }
    return render(request, 'txt2img/home.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def generate_image(request):
    """Generate image from text prompt"""
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return JsonResponse({
                'success': False,
                'error': 'Prompt is required'
            }, status=400)
        
        if len(prompt) > 500:
            return JsonResponse({
                'success': False,
                'error': 'Prompt is too long (max 500 characters)'
            }, status=400)
        
        logger.info(f"Generating image for prompt: {prompt}")
        
        # Generate image using Stable Diffusion
        image, generation_time = stable_diffusion_service.generate_image(
            prompt=prompt,
            width=512,
            height=512,
            num_inference_steps=20,
            guidance_scale=7.5
        )
        
        # Save image to database
        generated_image = GeneratedImage(
            prompt=prompt,
            generation_time=generation_time
        )
        
        # Convert PIL image to Django file
        img_io = io.BytesIO()
        image.save(img_io, format='PNG')
        img_file = ContentFile(img_io.getvalue(), name=f"{uuid.uuid4()}.png")
        
        generated_image.image.save(f"{uuid.uuid4()}.png", img_file, save=False)
        generated_image.save()
        
        return JsonResponse({
            'success': True,
            'image_url': generated_image.image.url,
            'generation_time': round(generation_time, 2),
            'prompt': prompt
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to generate image. Please try again.'
        }, status=500)
