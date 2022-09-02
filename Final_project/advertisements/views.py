from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AdFilter, FeedbackFilter
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
        # вписываем наш фильтр (AdFilter) в контекст
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

    def post(self, request, *args, **kwargs):
        """
        Метод переопределен для отправки письма по поводу создания отклика на объявление.
        Письмо отправляется автору объявления.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        new_feedback = Feedback(
            text=request.POST['text'],
            ad_id=request.POST['ad'],
            author_id=request.POST['author'])
        new_feedback.save()
        send_mail(subject=f'Новый отклик на ваше объявление!',
                  message = f'На ваше объявление "{new_feedback.ad.title}" откликнулись: "{new_feedback.text}"',
                  from_email = None,  # здесь указываете почту, с которой будете отправлять (об этом попозже)
                  recipient_list = [new_feedback.ad.user.email])  # здесь список получателей. Например, секретарь, сам врач и т. д.'Привет',
        return redirect(request.META.get('HTTP_REFERER', '/'))

class AdCreate(CreateView, LoginRequiredMixin):
    """
    Класс представления для создания объявления.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    model = Advertisement
    template_name = 'ads/create.html'
    form_class = AdForm

    def get_initial(self):
        """
        Переопределение функции для автозаполнения поля "автор объявления"
        """
        initial = super().get_initial()
        user = self.request.user
        initial['user'] = user
        return initial

class AdUpdate(UpdateView, LoginRequiredMixin):
    template_name = 'ads/edit.html'
    form_class = AdForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertisement.objects.get(pk=id)

class AdDelete(DeleteView, LoginRequiredMixin):
    """
    Класс представления для удаления объявления.
    Наследован от встроенного дженерика.
    """
    template_name = 'ads/delete.html'
    queryset = Advertisement.objects.all()
    success_url = '/'

class UserPersonalAds(ListView, LoginRequiredMixin):
    """
    Класс представления для списка объявлений и откликов к ним.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    model = Feedback
    template_name = 'signup/user_ads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        user = self.request.user
        context['user_ads'] = user.advertisement_set.all
        user_feedbacks = Feedback.objects.filter(ad__user=user)
        context['user_feedbacks'] = user_feedbacks
        accepted_feedbacks = user_feedbacks.filter(acception=True)
        context['accepted_feedbacks'] = accepted_feedbacks
        # вписываем наш фильтр (AdFilter) в контекст
        context['filter'] = FeedbackFilter(self.request.GET, queryset=user_feedbacks)
        return context

def feedback_acception(request, **kwargs):
    """
    Функция принятия отклика на объявление.
    После принятия отклика на почту автора направляется уведомление.
    """
    feedback = Feedback.objects.get(pk=kwargs['pk'])
    feedback.acception = True
    feedback.save(update_fields=["acception"])
    send_mail(subject=f'{feedback.ad.user} принял ваш отклик!',
              message=feedback.text,
              from_email=None,
              recipient_list=[feedback.author.email])
    return redirect(request.META.get('HTTP_REFERER', '/'))

def feedback_rejection(request, **kwargs):
    """
        Функция отзыва отклика на объявление.
        После отклонения отклика на почту автора направляется уведомление.
        """
    feedback = Feedback.objects.get(pk=kwargs['pk'])
    feedback.acception = False
    feedback.save(update_fields=["acception"])
    send_mail(subject=f'{feedback.ad.user} отклонил ваш отклик!',
              message=feedback.text,
              from_email=None,
              recipient_list=[feedback.author.email])
    return redirect(request.META.get('HTTP_REFERER', '/'))