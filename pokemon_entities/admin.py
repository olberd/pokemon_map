from django.contrib import admin
from django.utils.safestring import mark_safe

from pokemon_entities.models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    fields = ('title_ru', 'title_en', 'title_jp', 'img_url', 'get_html_image', 'description', 'previous_evolution')
    list_display = ('title_ru', 'title_en', 'title_jp', 'img_url', 'get_html_image', 'description', 'previous_evolution')
    readonly_fields = ('get_html_image',)

    def get_html_image(self, obj):
        if obj.img_url:
            return mark_safe(f"<img src='{obj.img_url.url}' width=50>")

    get_html_image.short_description = 'Миниатюра'


@admin.register(PokemonEntity)
class PokemonEntity(admin.ModelAdmin):
    fields = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at', 'level', 'health', 'strength',
              'defense', 'stamina')
    list_display = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at', 'level', 'health', 'strength',
                    'defense', 'stamina')
