import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from authenticate.models import Topic,Musician,Album,Webpage,AccessRecord
from faker import Faker

fakedata = Faker()
topics = ['Search', 'Social', 'News', 'Games','Marketplace']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakedata.url()
        fake_date = fakedata.date()
        fake_name = fakedata.company()

        #create webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name= fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
