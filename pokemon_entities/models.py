from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Покемон', max_length=150)

    def __str__(self):
        return self.title
