# Text to Image Generator

A minimalist and professional web application that generates images from text descriptions using Stable Diffusion v1-4 via Hugging Face Inference API.

## Features

- 🎨 **AI-Powered Image Generation**: Uses Stable Diffusion v1-4 via Hugging Face API
- 🎯 **Minimalist UI**: Clean, professional interface with modern design
- 🚀 **Lightweight**: No heavy ML dependencies - uses cloud API
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🐳 **Docker Ready**: Easy deployment with Docker and Docker Compose
- 💾 **Image History**: View recently generated images
- ⚡ **Real-time Progress**: Live feedback during image generation
- 🌐 **Cloud-Powered**: No GPU required - powered by Hugging Face infrastructure

## Quick Start with Docker

### Prerequisites

- Docker and Docker Compose installed
- Hugging Face account and API token

### Setup

1. **Get your Hugging Face API Token**:
   - Visit [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token with "Read" permissions
   - Copy the token for use in configuration

2. **Clone and Deploy**:
   ```bash
   # Clone the repository
   git clone https://github.com/caid-and-cubs/Txt2Img.git
   cd Txt2Img

   # Update docker-compose.yml with your token
   # Replace 'your-huggingface-token-here' with your actual token

   # Build and run
   docker-compose up --build
   ```

3. **Access the Application**:
   - Open http://localhost:8000 in your browser
   - Start generating images!

## Local Development

### Prerequisites

- Python 3.11+
- pip
- Virtual environment (recommended)
- Hugging Face API token

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

# Create .env file
echo "HUGGINGFACE_API_TOKEN=your_token_here" > .env

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
HUGGINGFACE_API_TOKEN=hf_your_token_here
```

### Docker Environment

Update `docker-compose.yml` environment section:

```yaml
environment:
  - DEBUG=False
  - SECRET_KEY=your-production-secret-key
  - HUGGINGFACE_API_TOKEN=hf_your_token_here
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

## Production Deployment

### With Docker Compose (Recommended)

1. Clone the repository on your server
2. Update environment variables in `docker-compose.yml`
3. Run: `docker-compose up -d --build`
4. The application will be available on port 8000

### Manual Production Setup

1. Set `DEBUG=False` in settings
2. Configure a proper secret key
3. Set your Hugging Face API token
4. Set up a reverse proxy (nginx) for SSL termination
5. Use a production database (PostgreSQL) if needed

## System Requirements

### Minimum Requirements
- 1GB RAM
- 1 CPU core
- 2GB disk space
- Internet connection for API calls

### Recommended Requirements
- 2GB RAM
- 2 CPU cores
- 5GB disk space
- Stable internet connection

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

- **Generation Time**: Typically 10-30 seconds depending on API load
- **First Request**: May take longer if the model needs to load
- **Rate Limits**: Subject to Hugging Face API rate limits
- **No GPU Required**: Runs on any system with internet access

## Troubleshooting

### Common Issues

1. **Authentication Error**: Check your Hugging Face API token
2. **Model Loading**: Wait 10-20 seconds and retry
3. **Rate Limit**: Wait before making another request
4. **Network Error**: Check internet connection

### Getting API Token

1. Visit [Hugging Face](https://huggingface.co)
2. Sign up for a free account
3. Go to Settings → Access Tokens
4. Create a new token with "Read" permissions
5. Copy and use in your configuration

### Logs

```bash
# View Docker logs
docker-compose logs web

# View Django logs (local development)
tail -f logs/django.log
```

## Cost and Limits

- **Free Tier**: Hugging Face offers free API access with rate limits
- **No Infrastructure Costs**: No need for expensive GPU servers
- **Scalable**: Automatically scales with Hugging Face infrastructure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Tech Stack

- **Backend**: Django 5.1.4, Django REST Framework
- **AI Model**: Stable Diffusion v1-4 via Hugging Face Inference API
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Containerization**: Docker, Docker Compose
- **Deployment**: Gunicorn, WhiteNoise

## Credits

- Stable Diffusion model by CompVis
- Hugging Face for API infrastructure
- UI design inspired by modern minimalist principles
- Built with Django and powered by Hugging Face