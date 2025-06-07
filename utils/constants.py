from pathlib import Path
from django.core.validators import RegexValidator

# Constants for the Django project
BASE_DIR_MAIN = Path(__file__).resolve().parent.parent
BASE_DIR_MEDIA = BASE_DIR_MAIN / 'media'
MEDIA_PROJECT = BASE_DIR_MEDIA / 'project'
MEDIA_TAG = BASE_DIR_MEDIA / 'tag'

# Regular expression validators for various fields
PHONE_NUMBER_VALIDATOR = RegexValidator(
    regex=r'^\d{10,15}$',
    message='Type between 10 and 15 digits.',
)
     