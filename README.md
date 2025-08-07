# Text to Image

Application web simple pour générer des images à partir de texte via l'API Hugging Face.

## Installation

```bash
git clone https://github.com/caid-and-cubs/Txt2Img.git
cd Txt2Img
```

## Configuration

1. Obtenez votre token sur [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Modifiez `docker-compose.yml` avec votre token

## Lancement

```bash
docker-compose up --build
```

Accédez à http://localhost:8000

## Développement local

```bash
pip install -r requirements.txt
export HUGGINGFACE_API_TOKEN=hf_votre_token
python manage.py runserver
```

C'est tout ! 🎨