from django.db import models
from django.utils import timezone


class Advertiser(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(verbose_name='کلیک ها', default=0)
    views = models.IntegerField(verbose_name='بازدید ها', default=0)

    @property
    def ads(self):
        return self.ad_set.all()

    def __str__(self):
        return f'{self.name}'
