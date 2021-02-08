from django.contrib.auth.models import User


class Advertiser(User):

    @property
    def name(self):
        return self.username

    @property
    def ads(self):
        return self.ad_set.all()

    def __str__(self):
        return f'{self.username}'
