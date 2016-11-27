import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


BASE_DIR = os.path.dirname(__file__)

settings.configure(
    APPEND_SLASH=False,
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        'compressor',
    ),
    MIDDLEWARE=(),
    ROOT_URLCONF='sitebuilder.urls',
    SECRET_KEY='thesecretkey',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    STATICFILES_FINDERS=(
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ),
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
    STATIC_URL='/static/',
    TEMPLATES=[{
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (),
    }],
)

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
