# Text to Image Generator

A minimalist and professional web application that generates images from text descriptions using Stable Diffusion v1-5 AI model.

## Features

- 🎨 **AI-Powered Image Generation**: Uses Stable Diffusion v1-5 for high-quality image synthesis
- 🎯 **Minimalist UI**: Clean, professional interface with modern design
- 🚀 **Fast Performance**: Optimized for both GPU and CPU environments
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🐳 **Docker Ready**: Easy deployment with Docker and Docker Compose
- 💾 **Image History**: View recently generated images
- ⚡ **Real-time Progress**: Live feedback during image generation

## Quick Start with Docker

### Prerequisites

- Docker and Docker Compose installed
- (Optional) NVIDIA GPU with Docker GPU support for faster generation

### GPU-Enabled Deployment

```bash
# Clone the repository
git clone https://github.com/caid-and-cubs/Txt2Img.git
cd Txt2Img

# Build and run with GPU support
docker-compose up --build
```

### CPU-Only Deployment

If you don't have a GPU or NVIDIA Docker support:

```bash
# Edit docker-compose.yml and uncomment the CPU version
# Comment out the GPU version and uncomment web-cpu service

docker-compose up --build
```

### Manual CPU-Only Build

```bash
docker build -f Dockerfile.cpu -t txt2img-cpu .
docker run -p 8000:8000 -v $(pwd)/media:/app/media txt2img-cpu
```

## Local Development

### Prerequisites

- Python 3.11+
- pip
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/caid-and-cubs/Txt2Img.git
cd Txt2Img

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Usage

1. Open your browser and navigate to `http://localhost:8000`
2. Enter a descriptive text prompt in the input field
3. Click "Generate Image" and wait for the AI to create your image
4. View your generated image and generation time
5. Browse recent creations in the gallery below

### Example Prompts

- "A beautiful sunset over a mountain landscape, digital art"
- "A futuristic cityscape with flying cars, cyberpunk style"
- "A cute cat wearing a wizard hat, watercolor painting"
- "Abstract geometric patterns in blue and gold"

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
HUGGINGFACE_API_TOKEN=your-token-here  # Optional, for private models
```

### Docker Environment

Update `docker-compose.yml` environment section:

```yaml
environment:
  - DEBUG=False
  - SECRET_KEY=your-production-secret-key
```

## Production Deployment

### With Docker Compose (Recommended)

1. Clone the repository on your server
2. Update environment variables in `docker-compose.yml`
3. Run: `docker-compose up -d --build`
4. The application will be available on port 8000

### Manual Production Setup

1. Set `DEBUG=False` in settings
2. Configure a proper secret key
3. Set up a reverse proxy (nginx) for SSL termination
4. Use a production database (PostgreSQL) if needed
5. Configure static file serving

## System Requirements

### Minimum Requirements (CPU)
- 4GB RAM
- 2 CPU cores
- 10GB disk space

### Recommended Requirements (GPU)
- 8GB RAM
- NVIDIA GPU with 6GB+ VRAM
- 4 CPU cores
- 20GB disk space

## API Endpoints

- `GET /` - Main application interface
- `POST /generate/` - Generate image from text prompt

### Generate Image API

```bash
curl -X POST http://localhost:8000/generate/ \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A beautiful landscape"}'
```

Response:
```json
{
  "success": true,
  "image_url": "/media/generated_images/uuid.png",
  "generation_time": 15.67,
  "prompt": "A beautiful landscape"
}
```

## Performance Notes

- **GPU**: Generation typically takes 5-20 seconds
- **CPU**: Generation may take 1-5 minutes depending on hardware
- First generation takes longer due to model loading
- Model is cached after first use

## Troubleshooting

### Common Issues

1. **Out of Memory**: Reduce image size or use CPU-only mode
2. **Slow Generation**: Ensure GPU drivers are properly installed
3. **Model Download Fails**: Check internet connection and disk space

### Logs

```bash
# View Docker logs
docker-compose logs web

# View Django logs (local development)
tail -f logs/django.log
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Tech Stack

- **Backend**: Django 5.1.4, Django REST Framework
- **AI Model**: Stable Diffusion v1-5 via Diffusers
- **ML Framework**: PyTorch
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Containerization**: Docker, Docker Compose
- **Deployment**: Gunicorn, WhiteNoise

## Credits

- Stable Diffusion model by Runway ML
- UI design inspired by modern minimalist principles
- Built with Django and PyTorch