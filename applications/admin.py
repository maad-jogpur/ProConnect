from django.contrib import admin
from . models import Application
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','user','created_at')

admin.site.register(Application,ApplicationAdmin)