from django.urls import path
from .views import AdvertisementList, AdvertisementDetail

urlpatterns = [
    # Представляем наш класс списка объявлений(AdvertisementList из view.py) при помощи метода as_view.
    path('', AdvertisementList.as_view(), name='ads_list'),
    # pk — это первичный ключ объявления, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', AdvertisementDetail.as_view(), name='ad_detail')
    ]