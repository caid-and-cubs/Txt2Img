# Text to Image

Application web simple pour générer des images à partir de texte via l'API Hugging Face.

## ⚠️ Configuration Obligatoire

**IMPORTANT**: Cette app nécessite un token Hugging Face gratuit.

### 1. Obtenez votre token

1. Créez un compte sur [huggingface.co](https://huggingface.co) (gratuit)
2. Allez dans [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Cliquez "New token" → "Read" → "Create token"
4. Copiez le token (commence par `hf_`)

### 2. Configurez le token

**Option A: Docker (recommandé)**
```bash
# Modifiez docker-compose.yml ligne 7 :
HUGGINGFACE_API_TOKEN=hf_votre_token_ici
```

**Option B: Variable d'environnement**
```bash
export HUGGINGFACE_API_TOKEN=hf_votre_token_ici
```

## Installation

```bash
git clone https://github.com/caid-and-cubs/Txt2Img.git
cd Txt2Img
```

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

## Dépannage

- **Erreur 401** : Token manquant ou invalide
- **Erreur 503** : Modèle en chargement, attendez 20s
- **Token invalide** : Doit commencer par `hf_`

C'est tout ! 🎨