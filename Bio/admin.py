from django.contrib import admin
from Bio.models import Bio
# Register your models here.

class BioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bio, BioAdmin)


