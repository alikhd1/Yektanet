from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('click/<int:ad_id>/', views.AdView.as_view(), name='ad'),
    path('new/', views.NewAdView.as_view(), name='newAd'),

]
