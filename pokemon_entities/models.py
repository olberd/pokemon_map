from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Покемон', max_length=150)
    photo = models.ImageField(upload_to='pokemons', null=True)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE)
