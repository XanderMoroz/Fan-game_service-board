from django.contrib.auth import views
from django.urls import path

from .views import BaseRegisterView

urlpatterns = [
    path('', BaseRegisterView.as_view(template_name='signup/signup.html'), name='signup'),
]
