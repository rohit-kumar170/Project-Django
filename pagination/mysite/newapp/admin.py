from django.contrib import admin
from .models import Movies
# Register your models here.

@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','rating']
