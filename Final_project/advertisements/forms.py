from django import forms
from django.forms import ModelForm
from .models import Advertisement, Feedback

class AdForm(ModelForm):
    """
    Форма для создания объявления
    """
    class Meta:
        """
        В класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля.
        Мы уже делали что-то похожее с фильтрами.
        """
        model = Advertisement
        fields = [
            'title',
            'content',
            'category',
            'user'
                ]
        labels = {
            'title': "Название объявления",
            'content': "Содержание",
            'category': "Категории",
        }

        widgets = {'user': forms.HiddenInput()}