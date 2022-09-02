from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm
from .models import Advertisement, Feedback

class AdForm(ModelForm):
    """
    Форма для создания объявления
    """
    content = forms.CharField(widget=CKEditorWidget, label='Содержание объявления')
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
            'title': "Заголовок",
            'content': "Содержание",
            'category': "Категория",
        }

        widgets = {'user': forms.HiddenInput()}

class FeedbackForm(ModelForm):
    """
    Форма для создания отклика на объявление
    """
    class Meta:
        model = Feedback
        fields = [
            'text',
            'ad',
            'author'
                ]
        labels = {
            'text': "Текст отклика",
        }

        widgets = {'author': forms.HiddenInput(),
                   'ad': forms.HiddenInput(),
                   }
