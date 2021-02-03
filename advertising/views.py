from django.shortcuts import render, get_object_or_404, redirect

from user.models import Advertiser
from .models import Ad

from .forms import NewAd


def index(request):
    advertisers = Advertiser.objects.all()
    for advertiser in advertisers:
        for ad in advertiser.ads:
            ad.views += 1
            ad.save()

    return render(request, 'advertising/ads.html', {'advertisers': advertisers})


def ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.clicks += 1
    ad.advertiser.clicks += 1
    ad.advertiser.save()
    ad.save()

    return redirect(ad.link)


def new_ad(request):
    if request.method == 'POST':
        form = NewAd(request.POST, request.FILES)
        if form.is_valid():
            advertiser = get_object_or_404(Advertiser, pk=form.cleaned_data.get('advertiser_id'))
            ad = Ad(
                title=form.cleaned_data.get('title'),
                link=form.cleaned_data.get('link'),
                img=form.cleaned_data.get('image'),
                advertiser=advertiser
            )
            ad.save()

    else:
        form = NewAd()

    return render(request, 'advertising/new_ad.html', {'form': form})
