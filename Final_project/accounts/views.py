from django.shortcuts import render
from django.views.generic import ListView

from Final_project.advertisements.models import Advertisement

"""
доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, 
удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление).
"""
# Create your views here.


class UserProfileView(ListView):
    # Указываем модель, объекты которой мы будем выводить (Объявление)
    model = Advertisement
    # Поле, которое будет использоваться для сортировки объявлений
    ordering = '-creation_date'
    # Указываем имя шаблона, в котором будут все инструкции к показу объявлений
    template_name = 'accounts/profile.html'
    # Слово, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'user_advertisement_list'