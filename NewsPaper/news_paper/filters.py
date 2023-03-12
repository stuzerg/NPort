import django_filters
from django_filters import FilterSet,  DateRangeFilter
from django_filters.widgets import RangeWidget

from .models import Post

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   # model = Post
   creation_date = django_filters.DateFromToRangeFilter( label='дата публикации', widget=RangeWidget(attrs={'type': 'date'}))
   header = django_filters.CharFilter( label='заголовок содержит', lookup_expr='icontains')
   author__user__username = django_filters.CharFilter( label='в имени автора присутствует ', lookup_expr='icontains')

