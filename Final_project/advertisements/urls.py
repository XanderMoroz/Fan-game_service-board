from django.urls import path
from .views import AdvertisementList, AdvertisementDetail, AdCreate, AdUpdate, AdDelete

urlpatterns = [
    # Представляем наш класс списка объявлений(AdvertisementList из view.py) при помощи метода as_view.
    path('', AdvertisementList.as_view(), name='ads_list'),
    # pk — это первичный ключ объявления, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', AdvertisementDetail.as_view(), name='ad_detail'),

    path('create', AdCreate.as_view(), name='create_advertisement'),
    path('edit/<int:pk>', AdUpdate.as_view(), name='update_advertisement'),
    path('delete/<int:pk>', AdDelete.as_view(), name='delete_advertisement'),
    ]