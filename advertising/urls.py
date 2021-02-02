from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('click/<int:ad_id>/', views.ad, name='ad'),
    path('new/', views.new_ad, name='newAd'),

]
