from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AdFilter
from .forms import AdForm, FeedbackForm
from .models import Advertisement, Feedback


# Create your views here.

class AdvertisementList(ListView):
    # Указываем модель, объекты которой мы будем выводить (Объявление)
    model = Advertisement
    # Поле, которое будет использоваться для сортировки объявлений
    ordering = '-creation_date'
    # Указываем имя шаблона, в котором будут все инструкции к показу объявлений
    template_name = 'ads/ads_list.html'
    # Слово, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'all_advertisement_list'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

class Search(ListView):
    model = Advertisement
    template_name = 'ads/search.html'
    context_object_name = 'search_list'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # вписываем наш фильтр (PostFilter) в контекст
        context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdFilter(self.request.GET, queryset=queryset).qs

class AdvertisementDetail(DetailView, CreateView):
    model = Advertisement
    # Используем шаблон — ad_detail.html
    template_name = 'ads/ad_detail.html'
    # Название объекта, в котором будет выбранное пользователем объявление
    context_object_name = 'ad_detail'
    #success_url =
    form_class = FeedbackForm

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        ad = Advertisement.objects.get(id=self.kwargs['pk'])
        #author = Author.objects.get(user_id=user.pk)
        initial['author'] = user
        initial['ad'] = ad
        return initial

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим список связанных с объявлением откликов'.
        ad = Advertisement.objects.get(id=self.kwargs['pk'])
        context['feedbacks'] = ad.feedback_set.all
        return context

class AdCreate(CreateView):
    """
    Класс представления для создания объявления.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    # permission_required = ('ads.add_post',)
    model = Advertisement
    template_name = 'ads/create.html'
    form_class = AdForm

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        #author = Author.objects.get(user_id=user.pk)
        initial['user'] = user
        return initial

class AdUpdate(UpdateView):
    template_name = 'ads/edit.html'
    form_class = AdForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertisement.objects.get(pk=id)

class AdDelete(DeleteView):
    """
    Класс представления для удаления объявления.
    Наследован от встроенного дженерика.
    """
    template_name = 'ads/delete.html'
    queryset = Advertisement.objects.all()
    success_url = '/ads/'