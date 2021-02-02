from django.shortcuts import render, get_object_or_404, redirect

from user.models import Advertiser
from .models import Ad



def index(request):
    advertisers = Advertiser.objects.all()
    return render(request, 'advertising/ads.html', {'advertisers': advertisers})


def ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.clicks += 1
    ad.advertiser.clicks += 1
    ad.advertiser.save()
    ad.save()

    return redirect(ad.link)


def redirect_view(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.clicks += 1
    ad.advertiser.clicks += 1
    ad.advertiser.save()
    ad.save()

    return HttpResponseRedirect(f'../../click/{ad_id}/')
