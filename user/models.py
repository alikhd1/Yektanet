from django.contrib.auth.models import User
from django.db import models


class Advertiser(User):
    clicks = models.IntegerField(verbose_name='کلیک ها', default=0)
    views = models.IntegerField(verbose_name='بازدید ها', default=0)

    @property
    def ads(self):
        return self.ad_set.all()

    def __str__(self):
        return f'{self.username}'
