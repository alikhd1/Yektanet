from django.db import models
from django.utils import timezone


from user.models import Advertiser


class Ad(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=100)
    link = models.CharField(verbose_name='لینک', max_length=200)
    img = models.ImageField(verbose_name='عکس', upload_to='ad_pic/')
    creation_date = models.DateTimeField(default=timezone.now)
    advertiser = models.ForeignKey(Advertiser, verbose_name='تبلیغ دهنده', on_delete=models.CASCADE)

    @property
    def image(self):
        return f'media/{self.img.name}'

    @property
    def clicks(self):
        return self.eventtracking_set.filter(event='ck')

    @property
    def views(self):
        return self.eventtracking_set.filter(event='vi')

    views_counts = views

    def __str__(self):
        return f'{self.title}'
