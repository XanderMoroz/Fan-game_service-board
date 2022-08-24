from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advertisement
# Create your views here.

class AdvertisementList(ListView):
    # Указываем модель, объекты которой мы будем выводить (Объявление)
    model = Advertisement
    # Поле, которое будет использоваться для сортировки объявлений
    ordering = 'creation_date'
    # Указываем имя шаблона, в котором будут все инструкции к показу объявлений
    template_name = 'ads/ads_list.html'
    # Слово, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'all_advertisement_list'

class AdvertisementDetail(DetailView):
    model = Advertisement
    # Используем шаблон — ad_detail.html
    template_name = 'ads/ad_detail.html'
    # Название объекта, в котором будет выбранное пользователем объявление
    context_object_name = 'ad_detail'