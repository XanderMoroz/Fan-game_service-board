from django.forms import DateInput
from django_filters import FilterSet, DateFilter, \
    CharFilter, TypedChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Advertisement


# создаём фильтр
class AdFilter(FilterSet):
    """
    creation_date = DateFilter(
        field_name='creation_date',
        label='Опубликованы позже',
        lookup_expr='gt',  # должна быть позже или равна тому (greater than), что указал пользователь
        widget=DateInput(format='%d.%m.%Y', attrs={'type': 'date', 'class': 'inp'})
    )
    title = CharFilter(
        label='Название',
        lookup_expr='contains'  # должно быть похожее на запрос пользователя
    )

    category = TypedChoiceFilter(
        label='Категории',
        choices=[(1, 'Fashion'), (2, 'History '), (3, 'Science'), (4, 'Movies')],
        widget=Select(attrs={'class': 'inp'})
    """


    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'creation_date',)  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
