from django.contrib import admin
from authenticate.models import Topic,Musician,Album,AccessRecord,Webpage

admin.site.register(Topic)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
