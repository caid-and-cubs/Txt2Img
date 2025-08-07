import requests
import os

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

def generate_image(prompt):
    """Génère une image via l'API Hugging Face"""
    token = os.getenv('HUGGINGFACE_API_TOKEN')
    
    if not token:
        raise Exception("Token Hugging Face manquant. Configurez HUGGINGFACE_API_TOKEN dans l'environnement.")
    
    if not token.startswith('hf_'):
        raise Exception("Token Hugging Face invalide. Il doit commencer par 'hf_'")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=60)
        
        if response.status_code == 200:
            return response.content
        elif response.status_code == 401:
            raise Exception("Token Hugging Face invalide ou expiré. Vérifiez votre token sur https://huggingface.co/settings/tokens")
        elif response.status_code == 503:
            raise Exception("Modèle en cours de chargement. Attendez 20 secondes et réessayez.")
        else:
            raise Exception(f"Erreur API Hugging Face ({response.status_code}): {response.text}")
    
    except requests.exceptions.Timeout:
        raise Exception("Timeout - L'API met trop de temps à répondre")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur de connexion: {str(e)}")