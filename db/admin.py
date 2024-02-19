from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Table)
class PostAdmin(admin.ModelAdmin):
    list_display = [ "name", 'date']