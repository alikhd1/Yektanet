from django.db import models
from django.utils import timezone

from .ad import Ad


class EventTracking(models.Model):
    AD_EVENTS = (
        ('ck', 'click'),
        ('vi', 'view'),
    )

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='تبلیغ')
    event = models.CharField(max_length=2, choices=AD_EVENTS, verbose_name='نوع رویداد')
    date = models.DateTimeField(default=timezone.now, verbose_name='زمان رویداد')
    visitor_ip = models.GenericIPAddressField(verbose_name='آیپی بازدید کننده', null=True)

    def __str__(self):
        return f'{self.ad}:{self.event}'
