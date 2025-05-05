import os
import sys
from pathlib import Path
from datetime import datetime
from pprint import pprint
from random import randint, sample
import django
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
    
    from project.models import Project, Tags
    
    start = datetime.now()
    
    print('Apagando DB')
    Project.objects.all().delete()
    Tags.objects.all().delete()
    
    fake = faker.Faker('pt-BR')
    possible_tags = ['Django', 'Python', 'Pandas', 'Jupiter', 'NETBeans', 'React', 'HTML', 'CSS', 'JS', 'Java', 'MongoDB', 'Docker']
    n = len(possible_tags)
    tags = sample(possible_tags, n) if NUMBER_OF_TAGS >= n else sample(possible_tags, NUMBER_OF_TAGS)
    
    django_tags = []
    
    for i in tags:
        desc_short = fake.text(max_nb_chars=200)
        desc_long = fake.text(max_nb_chars=randint(300, 800))
        created_date: datetime = fake.date_this_year() # type: ignore
        
        tag = Tags(
                name=i,
                desc_short=desc_short,
                desc_long=desc_long,
                created_at=created_date,
                updated_at='',
            )
        
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