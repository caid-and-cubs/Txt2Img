# views.py
import requests
import base64
import io
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import uuid
import time

def index(request):
    """Render the main page"""
    return render(request, 'general.html')

@csrf_exempt
@api_view(['POST'])
def generate_image(request):
    """Generate image using Stable Diffusion API"""
    try:
        # Get prompt from request
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        prompt = data.get('prompt', '')
        
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Prepare headers for Hugging Face API
        headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}",
            "Content-Type": "application/json"
        }
        
        # Prepare payload
        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": 50,
                "guidance_scale": 7.5,
                "width": 512,
                "height": 512
            }
        }
        
        # Make request to Hugging Face API
        response = requests.post(
            settings.STABLE_DIFFUSION_MODEL_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 503:
            # Model is loading, wait and retry
            estimated_time = response.json().get('estimated_time', 20)
            return Response({
                'status': 'loading',
                'estimated_time': estimated_time,
                'message': 'Model is loading, please try again in a few seconds'
            }, status=status.HTTP_202_ACCEPTED)
        
        if response.status_code != 200:
            return Response({
                'error': f'API request failed: {response.status_code}',
                'details': response.text
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Save the generated image
        image_data = response.content
        image_name = f"TrainEdge_{uuid.uuid4()}.png"
        
        # Save to media folder
        image_path = default_storage.save(
            f'imgstore/{image_name}',
            ContentFile(image_data)
        )
        
        # Return the image URL
        image_url = default_storage.url(image_path)
        
        return Response({
            'success': True,
            'image_url': image_url,
            'prompt': prompt,
            'generated_at': time.time()
        })
        
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
    except requests.exceptions.RequestException as e:
        return Response({'error': f'Request failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'error': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def check_model_status(request):
    """Check if the Stable Diffusion model is ready"""
    try:
        headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}",
        }
        
        # Send a simple test request
        response = requests.post(
            settings.STABLE_DIFFUSION_MODEL_URL,
            headers=headers,
            json={"inputs": "test"},
            timeout=10
        )
        
        if response.status_code == 503:
            return Response({
                'status': 'loading',
                'estimated_time': response.json().get('estimated_time', 20)
            })
        elif response.status_code == 200:
            return Response({'status': 'ready'})
        else:
            return Response({
                'status': 'error',
                'message': f'Status code: {response.status_code}'
            })
            
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        })

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({
        'status': 'healthy',
        'timestamp': time.time(),
        'version': '1.0.0'
    })

# Create your views here.
