DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'encurtador',
    }
}

TIME_ZONE = 'America/Recife'
LANGUAGE_CODE = 'pt-br'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

SECRET_KEY = 'x3%xv675kb9jy$vpif7&-zp*g@3wz*a91v4t92ktpjwekabm%c'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    'templates',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'encurtador.urls'

INSTALLED_APPS = (
    'djangotoolbox',
	'encurtador.redirecionamento',
)
