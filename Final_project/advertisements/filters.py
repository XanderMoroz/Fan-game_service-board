from django.forms import DateInput
from django_filters import FilterSet, DateFilter, \
    CharFilter, TypedChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Advertisement, Feedback


# создаём фильтр
class AdFilter(FilterSet):
    title = CharFilter(
        label='Заголовок',
        lookup_expr='contains'  # должно быть похожее на запрос пользователя
    )
    creation_date = DateFilter(
        field_name='creation_date',
        label='Опубликованы позже',
        lookup_expr='gt',  # должна быть позже или равна тому (greater than), что указал пользователь
        widget=DateInput(format='%d.%m.%Y', attrs={'type': 'date', 'class': 'inp'}))
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'creation_date',)  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)

class FeedbackFilter(FilterSet):
    creation_date = DateFilter(
        field_name='creation_date',
        label='Опубликованы позже',
        lookup_expr='gt',  # должна быть позже или равна тому (greater than), что указал пользователь
        widget=DateInput(format='%d.%m.%Y', attrs={'type': 'date', 'class': 'inp'}))

    class Meta:
        model = Feedback
        fields = ('ad', 'creation_date')