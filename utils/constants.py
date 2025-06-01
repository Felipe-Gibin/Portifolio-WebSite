from pathlib import Path

BASE_DIR_MAIN = Path(__file__).resolve().parent.parent
BASE_DIR_MEDIA = BASE_DIR_MAIN / 'media'
MEDIA_PROJECT = BASE_DIR_MEDIA / 'project'
MEDIA_TAG = BASE_DIR_MEDIA / 'tag'

if __name__ == '__main__':
    new_name = 'sla.jpg'
    project_path = MEDIA_PROJECT / new_name
    
    print(isinstance(project_path, Path))   