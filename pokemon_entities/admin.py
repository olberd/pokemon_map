from django.contrib import admin

from pokemon_entities.models import Pokemon


@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    list_display = ('title',)
