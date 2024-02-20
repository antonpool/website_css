from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Table)
class TableClassAdmin(admin.ModelAdmin):
    list_display = [ "name", 'date']
    prepopulated_fields = {'slug' : ('name',) } #автозаполнение поле slug
    