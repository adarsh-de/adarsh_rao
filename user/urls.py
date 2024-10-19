from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('songs/',views.songs),
    path('friends/',views.friends),
    path('foods/',views.foods),
    path('family/',views.family),
    path('special/',views.special),
    path('gallery/',views.gallery),
    path('favourite/',views.favourite),
    path('pictures/',views.pictures),
    path('movie/',views.movie),



]