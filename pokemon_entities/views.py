import folium
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404
from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    local_time = localtime()
    entities = PokemonEntity.objects.filter(appeared_at__lte=local_time, disappeared_at__gte=local_time)
    for entity in entities:
        add_pokemon(
            folium_map, entity.lat,
            entity.lon,
            entity.pokemon.img_url.path,
        )
    pokemons_on_page = []
    pokemons_all = Pokemon.objects.all()
    for pokemon in pokemons_all:
        pokemons_on_page.append({
            'id': pokemon.id,
            'title_ru': pokemon.title_ru,
            'image': pokemon.img_url.url if pokemon.img_url else DEFAULT_IMAGE_URL,
        })
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_entities = pokemon.entities.all()

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': pokemon.img_url.url if pokemon.img_url else DEFAULT_IMAGE_URL,
    }
    previous_evolution = pokemon.previous_evolution
    if previous_evolution:
        pokemon_data['previous_evolution'] = {
            'pokemon_id': previous_evolution.id,
            'title_ru': previous_evolution.title_ru,
            'img_url': previous_evolution.img_url.url if previous_evolution.img_url else DEFAULT_IMAGE_URL,
        }
    next_evolution = pokemon.next_evolutions.first()
    if next_evolution:
        pokemon_data['next_evolution'] = {
            'pokemon_id': next_evolution.id,
            'title_ru': next_evolution.title_ru,
            'img_url': next_evolution.img_url.url if next_evolution.img_url else DEFAULT_IMAGE_URL,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.img_url.path,
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data
    })
