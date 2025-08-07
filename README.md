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

**⚠️ SÉCURITÉ**: Ne jamais committer votre vrai token !

**Option A: Docker (recommandé)**
```bash
# 1. Modifiez docker-compose.yml ligne 8 :
HUGGINGFACE_API_TOKEN=hf_votre_token_ici

# 2. Ou utilisez une variable d'environnement :
export HUGGINGFACE_API_TOKEN=hf_votre_token_ici
docker-compose up --build
```

**Option B: Fichier .env**
```bash
# 1. Copiez le fichier d'exemple :
cp .env.example .env

# 2. Éditez .env avec votre token :
HUGGINGFACE_API_TOKEN=hf_votre_token_ici
```

## Installation

```bash
git clone https://github.com/caid-and-cubs/Txt2Img.git
cd Txt2Img
```

## Lancement

```bash
# Configurez d'abord votre token (voir ci-dessus), puis :
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

## 🔒 Sécurité

- ✅ Utilisez `.env` pour les secrets
- ✅ Ajoutez `.env` au `.gitignore`
- ❌ Ne commitez jamais de vrais tokens

C'est tout ! 🎨