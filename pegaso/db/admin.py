from django.contrib import admin

from .models import Project, Airplane, UserProfile, OperatorProfile, Mission

# Register your models here.

admin.site.register(Project)
admin.site.register(Airplane)
admin.site.register(UserProfile)
admin.site.register(OperatorProfile)
# TODO: Add script to reset all yearly hours

admin.site.register(Mission)


