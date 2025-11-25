"""
Test settings for demoDjango project.
"""
from .settings import *

# Override settings for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory database for tests
    }
}

# Disable migrations for faster testing
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Additional test-specific settings
SECRET_KEY = 'django-insecure-test-key-for-testing-only'
DEBUG = True
