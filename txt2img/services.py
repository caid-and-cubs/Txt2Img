import requests
from PIL import Image
import io
import time
import logging
import base64
from django.conf import settings

logger = logging.getLogger(__name__)


class HuggingFaceStableDiffusionService:
    """Service class for Hugging Face Stable Diffusion API"""
    
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
        self.headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"
        }
    
    def generate_image(self, prompt, **kwargs):
        """
        Generate an image from text prompt using Hugging Face API
        
        Args:
            prompt (str): Text description of the image to generate
            
        Returns:
            tuple: (PIL Image, generation_time)
        """
        start_time = time.time()
        
        try:
            logger.info(f"Generating image for prompt: {prompt}")
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "guidance_scale": 7.5,
                    "num_inference_steps": 20,
                    "width": 512,
                    "height": 512
                }
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=60  # 60 seconds timeout
            )
            
            if response.status_code == 200:
                # The response contains the image bytes
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))
                
                generation_time = time.time() - start_time
                logger.info(f"Image generated successfully in {generation_time:.2f} seconds")
                
                return image, generation_time
            
            elif response.status_code == 503:
                # Model is loading, retry after a short wait
                logger.warning("Model is loading, retrying in 10 seconds...")
                time.sleep(10)
                return self.generate_image(prompt, **kwargs)
            
            else:
                error_msg = f"API request failed with status {response.status_code}: {response.text}"
                logger.error(error_msg)
                raise Exception(error_msg)
                
        except requests.exceptions.Timeout:
            error_msg = "Request timeout - the API took too long to respond"
            logger.error(error_msg)
            raise Exception(error_msg)
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Network error: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)
            
        except Exception as e:
            error_msg = f"Failed to generate image: {str(e)}"
            logger.error(error_msg)
            raise e


# Global instance
stable_diffusion_service = HuggingFaceStableDiffusionService()