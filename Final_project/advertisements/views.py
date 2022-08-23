from django.shortcuts import render
from django.views.generic import ListView
from .models import Advertisement
# Create your views here.

class AdvertisementList(ListView):
    # Указываем модель, объекты которой мы будем выводить (Объявление)
    model = Advertisement
    # Поле, которое будет использоваться для сортировки объявлений
    ordering = 'creation_date'
    # Указываем имя шаблона, в котором будут все инструкции о том, как должны быть показаны объявления
    template_name = 'ads_list.html'
    # Слово, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'Advertisements'