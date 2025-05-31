import os
import sys
from pathlib import Path
from datetime import datetime
from pprint import pprint
from random import randint, sample, choice
import django
from django.core.files import File
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_PROJECTS = 50
NUMBER_OF_TAGS = 15
NUMBER_OF_T_IN_P = 7

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
settings.USE_TZ = False
django.setup()

if __name__ == '__main__':
    '''
    CUIDADO!!!!!
    Apagará todo o banco de dados
    e injetará dados
    '''
    
    
    print('\n' * 10)
    print('--------------INICIANDO--------------')
    import faker
    from projects_app.models import Project, Tags
    start = datetime.now()
    
    IMG_PATHS = DJANGO_BASE_DIR / 'media' / 'icons_for_injection'
    
    print('Apagando DB')
    Project.objects.all().delete()
    Tags.objects.all().delete()
    
    fake = faker.Faker('pt-BR')
    possible_tags = ['Django', 'Python', 'Pandas', 'Jupiter', 'NETBeans', 'React', 'HTML', 'CSS', 'JS', 'Java', 'MongoDB', 'Docker']
    tag_data = [
        {"name": "Django", "img_path": 'django.jpeg'},
        {"name": "Python", "img_path": 'python.jpeg'},
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
    proj_icons = [f'P{i}.png'for i in range(1,8)]
    
    n = len(tag_data)
    django_tags = []
    
    for i in range(n):
        desc_short = fake.text(max_nb_chars=200)
        desc_long = fake.text(max_nb_chars=randint(300, 800))
        created_date: datetime = fake.date_this_year() # type: ignore
        
        tag = Tags(
                name=tag_data[i]['name'],
                desc_short=desc_short,
                desc_long=desc_long,
                created_at=created_date,
                updated_at='',
            )

        # Abre o arquivo de imagem e associa
        
        img_path = str(IMG_PATHS / tag_data[i]["img_path"])
        with open(img_path, 'rb') as f:
            tag.img_icon.save(tag_data[i]["img_path"], File(f), save=False)  
        tag.save()
        django_tags.append(tag)
        
    print('implementação das tags')
    pprint(django_tags)
    all_tags_list = list(Tags.objects.all())
        
    django_projects = []    
    for _ in range(NUMBER_OF_PROJECTS):
        name_project = " ".join(fake.words(nb=randint(1, 2))).title()
        desc_short = fake.text(max_nb_chars=400)
        desc_long = fake.text(max_nb_chars=randint(300, 1800))
        n = randint(1, min(NUMBER_OF_T_IN_P, len(django_tags)))
        selected_tags = sample(all_tags_list, n)
        
        created_date: datetime = fake.date_this_year() # type: ignore
        project = Project(
                name=name_project,
                short_desc=desc_short,
                long_desc=desc_long,
                created_at=created_date,
                updated_at='',
            )
        # Abre o arquivo de imagem e associa
        r_file_name = choice(proj_icons)
        img_path = str(IMG_PATHS / r_file_name)
        with open(img_path, 'rb') as f:
            project.img_icon.save(r_file_name, File(f), save=False)
        project.save()
        project.tags.set(selected_tags)
        django_projects.append(project)
        
    print('implementação dos projetos')
    pprint(django_projects)
    
    end = datetime.now()
    delta = end - start
    print(f'Tempo total: {delta.total_seconds():.3f}s' )
    print(f'Total tags: {len(django_tags)} --- Total Projects: {len(django_projects)}' )
    print('--------------FIM--------------')