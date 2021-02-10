from django.views.generic import CreateView

from advertising.models import Ad


class NewAdView(CreateView):
    model = Ad
    fields = ['advertiser', 'title', 'link', 'img']
    template_name = 'advertising/new_ad.html'
    success_url = '../'

    def form_valid(self, form):
        return super().form_valid(form)