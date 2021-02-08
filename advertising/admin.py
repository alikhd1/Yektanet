from django.contrib import admin

from advertising.models.ad import Ad
from advertising.models.tracking import EventTracking
# from user import Advertiser

admin.site.register(Ad)
admin.site.register(EventTracking)
# admin.site.register(Advertiser)

