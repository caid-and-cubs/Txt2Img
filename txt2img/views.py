from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from .services import generate_image

def home(request):
    """Page principale"""
    return render(request, 'home.html')

@csrf_exempt
def generate(request):
    """Génère une image"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt', '').strip()
            
            if not prompt:
                return HttpResponse('Prompt requis', status=400)
            
            # Générer l'image
            image_data = generate_image(prompt)
            
            # Retourner l'image directement
            response = HttpResponse(image_data, content_type='image/png')
            response['Content-Disposition'] = 'inline; filename="generated.png"'
            return response
            
        except Exception as e:
            return HttpResponse(f'Erreur: {str(e)}', status=500)
    
    return HttpResponse('Méthode non autorisée', status=405)
