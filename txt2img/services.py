import requests
import os

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

def generate_image(prompt):
    """Génère une image via l'API Hugging Face"""
    token = os.getenv('HUGGINGFACE_API_TOKEN')
    if not token:
        raise Exception("Token Hugging Face manquant")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Erreur API: {response.status_code}")