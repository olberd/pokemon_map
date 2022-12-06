from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(verbose_name='Покемон', max_length=150)
    title_en = models.CharField(verbose_name='Название на английском', max_length=150, blank=True)
    title_jp = models.CharField(verbose_name='Название на японском', max_length=150, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    img_url = models.ImageField('Изображение', null=True, blank=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='next_evolutions', verbose_name='Предыдущая эволюция')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE)


