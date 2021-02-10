from django.contrib.auth.models import User


class Advertiser(User):

    @property
    def name(self):
        return self.username

    def __str__(self):
        return f'{self.username}'
