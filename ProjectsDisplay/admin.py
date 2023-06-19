from django.contrib import admin
from ProjectsDisplay.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)