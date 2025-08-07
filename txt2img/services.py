import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import io
import time
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class StableDiffusionService:
    """Service class for Stable Diffusion image generation"""
    
    def __init__(self):
        self.pipeline = None
        self.model_id = "runwayml/stable-diffusion-v1-5"  # Using v1-5 as it's more stable
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    
    def load_model(self):
        """Load the Stable Diffusion model"""
        if self.pipeline is None:
            try:
                logger.info(f"Loading Stable Diffusion model on {self.device}")
                
                # Load the pipeline
                self.pipeline = StableDiffusionPipeline.from_pretrained(
                    self.model_id,
                    torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                    use_safetensors=True
                )
                
                # Move to device
                self.pipeline = self.pipeline.to(self.device)
                
                # Enable memory efficient attention if CUDA is available
                if self.device == "cuda":
                    self.pipeline.enable_attention_slicing()
                    # self.pipeline.enable_xformers_memory_efficient_attention()
                
                logger.info("Model loaded successfully")
                
            except Exception as e:
                logger.error(f"Failed to load model: {e}")
                raise e
    
    def generate_image(self, prompt, width=512, height=512, num_inference_steps=20, guidance_scale=7.5):
        """
        Generate an image from text prompt
        
        Args:
            prompt (str): Text description of the image to generate
            width (int): Width of the generated image
            height (int): Height of the generated image
            num_inference_steps (int): Number of denoising steps
            guidance_scale (float): Guidance scale for generation
            
        Returns:
            tuple: (PIL Image, generation_time)
        """
        if self.pipeline is None:
            self.load_model()
        
        start_time = time.time()
        
        try:
            logger.info(f"Generating image for prompt: {prompt}")
            
            # Generate image
            with torch.autocast(self.device):
                result = self.pipeline(
                    prompt=prompt,
                    width=width,
                    height=height,
                    num_inference_steps=num_inference_steps,
                    guidance_scale=guidance_scale,
                    num_images_per_prompt=1
                )
            
            image = result.images[0]
            generation_time = time.time() - start_time
            
            logger.info(f"Image generated successfully in {generation_time:.2f} seconds")
            
            return image, generation_time
            
        except Exception as e:
            logger.error(f"Failed to generate image: {e}")
            raise e
    
    def cleanup(self):
        """Cleanup GPU memory"""
        if self.pipeline is not None and self.device == "cuda":
            torch.cuda.empty_cache()


# Global instance
stable_diffusion_service = StableDiffusionService()