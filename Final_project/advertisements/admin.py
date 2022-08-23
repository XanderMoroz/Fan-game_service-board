from django.contrib import admin
from .models import Advertisement, Feedback

# Подключили к админке модели:

admin.site.register(Advertisement)  # Объявление(Advertisement)
admin.site.register(Feedback)  # Отклик(Feedback)