from django.contrib import admin

from pokemon_entities.models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PokemonEntity)
class PokemonEntity(admin.ModelAdmin):
    list_display = ('lat', 'lon')
