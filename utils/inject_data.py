import os
import sys
from pathlib import Path

DJANGO_BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(DJANGO_BASE_DIR))

import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'portifolio_project.settings'
django.setup()

from projects_app.models import ProjectModel, TagModel
from random import randint, sample, choice
from django.core.files import File
from django.conf import settings
from utils.img_processor import process_img

NUMBER_OF_PROJECTS = 50
NUMBER_OF_TAGS = 15
NUMBER_OF_T_IN_P = 7

# NOTE: Set to True if you want to inject images into the projects and tags
WITH_IMG = True

# Define the path to the images for injection
# Assuming the images are stored in a directory named 'images_for_injection' inside the 'media' directory

if WITH_IMG:
    IMG_PATHS = DJANGO_BASE_DIR / 'media' / 'images_for_injection'

settings.USE_TZ = False

if __name__ == '__main__':
    import faker
    '''
    Warning: This script will delete all data in the ProjectModel and TagModel tables.
    It is intended for development purposes only to inject sample data into the database.
    '''
    print("Deleting existing data in ProjectModel and TagModel...")
    ProjectModel.objects.all().delete()
    TagModel.objects.all().delete()


    # Initialize Faker
    fake = faker.Faker('pt-BR')
    
    # Generate fake data for tags and projects
    # Define the tag data with names and image paths
    tag_data = [
        {"name": "Django", "img_path": 'django.png'},
        {"name": "Python", "img_path": 'python.png'},
        {"name": "css", "img_path": 'css.png'},
        {"name": "Pandas", "img_path": 'pandas.png'},
        {"name": "Jupyter", "img_path": 'jupyter.png'},
        {"name": "NETBeans", "img_path": 'netbeans.png'},
        {"name": "React", "img_path": 'react.png'},
        {"name": "HTML", "img_path": 'html.png'},
        {"name": "JS", "img_path": 'javascript.png'},
        {"name": "Java", "img_path": 'java.png'},
        {"name": "MongoDB", "img_path": 'mongodb.png'},
        {"name": "Docker", "img_path": 'docker.png'},
    ]
    
    if WITH_IMG:
        # Assuming you have 50 project icons in the media/images_for_injection directory
        proj_images = [f'free_img_{i}.jpg' for i in range(50)] 

    # Create tags
    print("Creating tags...")
    for tag_info in tag_data:
        short_desc = fake.text(max_nb_chars=200)
        long_desc = fake.text(max_nb_chars=randint(300, 800))

        tag = TagModel(
            name=tag_info['name'],
            short_desc=short_desc,
            long_desc=long_desc,
        )
        tag.save()

    print("Tags created successfully.")
    all_tags_list = list(TagModel.objects.all())

    # Create projects
    print("Creating projects...")
    for _ in range(NUMBER_OF_PROJECTS):
        name_project = " ".join(fake.words(nb=randint(1, 2))).title()
        short_desc = fake.text(max_nb_chars=400)
        long_desc = fake.text(max_nb_chars=randint(300, 1800))
        n_tags = randint(1, min(NUMBER_OF_T_IN_P, len(all_tags_list)))
        selected_tags = sample(all_tags_list, n_tags)

        project = ProjectModel(
            name=name_project,
            short_desc=short_desc,
            long_desc=long_desc,
        )
        project.save()
        # Assign random tags to the project
        project.tags.set(selected_tags)
        
    print("Projects created successfully.")
    
    if WITH_IMG:
        # Assign random icons to TagModel instances
        print("Assigning icons to tags...")
        for tag, tag_info in zip(TagModel.objects.all(), tag_data):
            img_path = IMG_PATHS / tag_info['img_path']
            print(f"Assigning icon {img_path} to tag {tag.name}")
            # Check if the image file exists before assigning
            if img_path.exists():
                with open(img_path, 'rb') as img_file:
                    tag.img_icon = File(img_file, name=img_path.name) # type: ignore
                    tag.save()
        print("Icons assigned to tags successfully.")
        # Assign random images to ProjectModel instances
        print("Assigning images to projects...")
        for project in ProjectModel.objects.all():
            img_path = IMG_PATHS / choice(proj_images)
            print(f"Assigning image {img_path} to project {project.name}")
            # Check if the image file exists before assigning
            if img_path.exists():
                with open(img_path, 'rb') as img_file:
                    project.img_icon = File(img_file, name=img_path.name)# type: ignore
                    project.save()
        
        print("Images assigned to projects successfully.")
    
    print("Data injection completed successfully.")