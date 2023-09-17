
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7@8*0a-o2&vh#$f3%o^5lg7n-v1z6&j3c5lw*m-u(^3o151f#^'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compte',
    'django_filters',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'projet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'liafashiongn',
        'PASSWORD':"",
        'HOST':'localhost',
        'PORT':'5433',
    }
}"""

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# ---------------    2.  Gestion des Fichiers Static   -----------------------
STATIC_URL = 'static/'
MEDIA_URL = 'media/'

if os.environ.get('ENV') == 'PRODUCTION':
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATICFILES_STORAGE = (
        'whitenoise.storage.CompressedManifestStaticFilesStorage',
    )


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



    # -------------------   A. Mise en Production   -------------------------------------

    # git init
    # git config --global user.name "Fassou CONDE"
    # git config --global user.email defassou@gmail.com
    # git status
    # git add *
    # git commit -m "Mise en Production"

    # -------------------   B. Track du fichier static file   -------------------------------------

    # Dans la console,dans le fichier static du projet, créer le fichier .gitignore en tapant:
    # touch projet/static/.gitignore
    # Coller dans le fichier gitignore: !.gitignore
    # Ajouter ce fichier en tapant: git add projet/static/.gitignore
    # Enfin: git commit -m "Track du fichier static file"

    # -------------------  C. Créer une application heroku       -------------------
    #  heroku create liafashion


    # -------------------  D.  Enregistrement des variables d'environnement   -------------------

    # heroku config:set SECRET_KEY="xxxxxxxxxx"
    # heroku config:set VENV="PRODUCTION"
    # heroku config

    # -------------------  E. Envoi sur le serveur/Pousser dans heroku  ------------------
    # git push heroku master

    # -------------------  F. Migration de la base de données  ------------------
    # heroku run python manage.py migrate

    #  ------------------  G. Création du superutilisateur    ------------------
    # heroku run python manage.py createsuperuser

    # ------------------  G.  Importation de la base de données    ------------------
    # heroku run python manage.py loaddata app/dumps/app.json

    # ----------------- Fin Code heroku ---------------------




# --------------------------  UTILISATION DE GIT ET GITHUB ---------------------------------
# ---------------  1. Dans la console GIT  -------------------

# Dans git bash, initialiser le projet:
# git init

# créer le fichier requirements.txt: pip freeze > requirements.txt
# git add *
# git commit -m "Mise en production"

# créer le fichier .gitignore dans le projet/static: touch projet/static/.gitignore
# Coller dans ce fichier: .idea/
# git add *
# git commit -m "Track static file(gitignore)"


# ------------ 2. Envoi sur le serveur github -----------------------------
# a.Se connecter à son compte github
# b.Créer un repository
# c.Créer un projet dans repository

# ------ Ajouter origin -----
# git remote
# git remote add origin url
# git remote (ceci affichera origin)

# ------ Ajouter Une branche -----
# Créer une branche(main) en tapant:
# git branch -M main
# git branch
# (pour vérifier)

# Basculer les fichiers du git(dépôt local) sur le github(dépôt distant)
# git push -u origin main
