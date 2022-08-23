from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Advertisement(models.Model):
    '''
    Эта модель описывает объявления, которые создают пользователи.
    Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент.
    Каждое объявление относится к одной из следующих категорий:
    Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
    может иметь одну или несколько категорий. Модель должна включать следующие поля:
    - поле связанное с пользователем(автором объявления);
    - поле с выбором категории объявления;
    - автоматически добавляемая дата и время создания объявления;
    - заголовок объявления;
    - текст объявления.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2,
                                choices=[('TN', 'Танки'), ('HE', 'Хилы'), ('DD', 'ДД'), ('ME', 'Торговцы'),
                                         ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BS', 'Кузнецы'),
                                         ('TR', 'Кожевники'), ('PM', 'Зельевары'), ('MS', 'Мастера заклинаний')],
                                default='TN',
                                verbose_name='Категория объявления')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = RichTextField(blank=True, null=True, verbose_name='Содержание')


class Feedback(models.Model):
    '''
    Эта модель описывает отклики на объявления, других пользователей. Отклик состоит из текста.
    Модель включает следующие поля:
        - поле связанное с пользователем(автором отклика);
        - поле связанное с объявлением(к которому добавлен отклик);
        - автоматически добавляемая дата и время создания отклика;
        - текст отклика.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    text = models.CharField(max_length=256, verbose_name='Текст отклика')