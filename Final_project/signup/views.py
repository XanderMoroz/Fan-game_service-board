from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


"""
доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, 
удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление).
"""

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('login')  # '/'


# Create your views here.



"""
class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/signup.html'
"""