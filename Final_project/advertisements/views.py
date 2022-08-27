from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AdForm
from .models import Advertisement
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

class AdvertisementDetail(DetailView):
    model = Advertisement
    # Используем шаблон — ad_detail.html
    template_name = 'ads/ad_detail.html'
    # Название объекта, в котором будет выбранное пользователем объявление
    context_object_name = 'ad_detail'

class AdCreate(CreateView):
    """
    Класс представления для создания объявления.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    #permission_required = ('news.add_post',)
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