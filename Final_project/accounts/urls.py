from django.contrib.auth import views
from django.urls import path

from Final_project.accounts.views import UserProfileView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile')
]