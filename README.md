# Stable Diffusion Django Web Application

A modern web application for generating images using Stable Diffusion v1.4 API, built with Django and deployed using Docker.

## ✨ Features

- 🎨 **AI Image Generation** - Generate images from text prompts using Stable Diffusion v1.4
- 🚀 **Modern UI** - Beautiful, responsive frontend with real-time feedback
- 🐳 **Docker Deployment** - Complete containerization with Docker Compose
- 🗄️ **PostgreSQL Database** - Robust data storage for generated images
- 🔧 **Admin Interface** - Django admin for managing generated content
- 📊 **API Usage Tracking** - Monitor API calls and performance
- 🔒 **Production Ready** - Nginx reverse proxy and security best practices

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Hugging Face API token (free at [huggingface.co](https://huggingface.co/settings/tokens))

### Installation

1. **Clone and setup the project:**
```bash
mkdir stable-diffusion-django
cd stable-diffusion-django
```

2. **Create the project structure and files** (use the provided code artifacts)

3. **Get your Hugging Face API token:**
   - Visit [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Create a new token (read permission is sufficient)
   - Copy the token

4. **Configure environment variables:**
```bash
# Edit .env file
HUGGINGFACE_API_TOKEN=your_actual_token_here
SECRET_KEY=your-super-secret-key-for-production
```

5. **Deploy with one command:**
```bash
chmod +x deploy.sh
./deploy.sh
```

## 🛠️ Manual Setup

If you prefer manual setup:

```bash
# Build containers
docker-compose build

# Start database
docker-compose up -d db

# Run migrations
docker-compose run --rm web python manage.py migrate

# Create superuser (optional)
docker-compose run --rm web python manage.py createsuperuser

# Collect static files
docker-compose run --rm web python manage.py collectstatic --noinput

# Start all services
docker-compose up -d
```

## 🌐 Access Points

- **Main Application:** http://localhost
- **Admin Interface:** http://localhost/admin
- **API Endpoints:**
  - `POST /api/generate/` - Generate images
  - `GET /api/status/` - Check model status
  - `GET /api/health/` - Health check

## 📡 API Usage

### Generate Image
```bash
curl -X POST http://localhost/api/generate/ \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A beautiful sunset over mountains"}'
```

### Check Model Status
```bash
curl http://localhost/api/status/
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Django secret key | Required |
| `HUGGINGFACE_API_TOKEN` | HF API token | Required |
| `DB_NAME` | Database name | `diffusion_db` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `postgres` |
| `ALLOWED_HOSTS` | Allowed hosts | `localhost,127.0.0.1` |

### Model Parameters

Modify in `views.py`:
```python
payload = {
    "inputs": prompt,
    "parameters": {
        "num_inference_steps": 50,  # Quality vs speed
        "guidance_scale": 7.5,      # Prompt adherence
        "width": 512,               # Image width
        "height": 512               # Image height
    }
}
```

## 🐳 Docker Commands

```bash
# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose build --no-cache

# Access Django shell
docker-compose exec web python manage.py shell

# Run Django commands
docker-compose exec web python manage.py <command>
```

## 🔍 Troubleshooting

### Common Issues

1. **Model Loading (503 Error)**
   - First API call may take 20+ seconds as model loads
   - Status endpoint shows loading progress

2. **Permission Errors**
   ```bash
   sudo chown -R $USER:$USER .
   chmod +x deploy.sh
   ```

3. **Database Connection Issues**
   ```bash
   docker-compose down
   docker volume rm stable-diffusion-django_postgres_data
   docker-compose up -d
   ```

4. **Static Files Not Loading**
   ```bash
   docker-compose exec web python manage.py collectstatic --clear
   ```

### Logs and Debugging

```bash
# Application logs
docker-compose logs web

# Database logs
docker-compose logs db

# Nginx logs
docker-compose logs nginx

# All services
docker-compose logs -f
```

## 📊 Production Deployment

For production deployment:

1. **Security Settings:**
   - Set `DEBUG=False`
   - Use strong `SECRET_KEY`
   - Configure proper `ALLOWED_HOSTS`
   - Set up HTTPS with Let's Encrypt

2. **Database:**
   - Use managed PostgreSQL service
   - Configure backup strategy

3. **Storage:**
   - Use cloud storage (AWS S3, Google Cloud Storage)
   - Configure CDN for static files

4. **Monitoring:**
   - Add logging and monitoring
   - Set up health checks
   - Configure alerts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) by CompVis
- [Hugging Face](https://huggingface.co) for API hosting
- [Django](https://djangoproject.com) web framework
- [Docker](https://docker.com) containerization