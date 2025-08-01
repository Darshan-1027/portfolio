from django.contrib import admin
from .models import *


class ShowPhoto(admin.ModelAdmin):
    list_display = ["photo_tag"]

admin.site.register(PhotoModel,ShowPhoto)


admin.site.register(NameModel)


admin.site.register(ResumeModel)

admin.site.register(skillmodel)

admin.site.register(filter)

admin.site.register(projectmodel)

admin.site.register(contactmodel)