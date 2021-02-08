from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, CreateView

from user.models import Advertiser
from .models.ad import Ad
from .models.tracking import EventTracking


class IndexView(TemplateView):
    template_name = 'advertising/ads.html'
    advertisers = Advertiser.objects.all()

    @classmethod
    def increaseView(cls):
        for advertiser in cls.advertisers:
            for ad in advertiser.ads:
                tracker = EventTracking(ad=ad, event='vi')
                tracker.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.increaseView()
        context['advertisers'] = self.advertisers

        return context


class AdView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        tracker = EventTracking(ad=ad, event='ck')
        tracker.save()

        self.url = ad.link

        return super().get_redirect_url(*args, **kwargs)


class NewAdView(CreateView):
    model = Ad
    fields = ['advertiser', 'title', 'link', 'img']
    template_name = 'advertising/new_ad.html'
    success_url = '../'

    def form_valid(self, form):
        return super().form_valid(form)
