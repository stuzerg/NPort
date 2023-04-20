
from django.urls import path
from django.views.decorators.cache import cache_page
# Импортируем созданное нами представление
from .views import PostList, PostListFiltered, PostNewsList, PostArticlesList, PostDetail, PostCreate, \
   PostEdit, PostDelete, CategorySubscribing

urlpatterns = [
   # path — означает путь.

   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('articles/', cache_page(10)(PostArticlesList.as_view()), name='post_list'),
   path('news/', PostNewsList.as_view(), name='post_list'),
   path('articles/search', PostListFiltered.as_view(), name='post_list'),
   path('news/search', PostListFiltered.as_view(), name='post_list'),


   path('articles/<int:pk>', PostDetail.as_view()),
   path('news/<int:pk>', PostDetail.as_view()),

   path('articles/create/', PostCreate.as_view(), name='post_create' ),
   path('articles/<int:pk>/edit', PostEdit.as_view()),
   path('articles/<int:pk>/delete', PostDelete.as_view() ),

   path('news/create/', PostCreate.as_view(), name='post_create' ),
   path('news/<int:pk>/edit', PostEdit.as_view()),
   path('news/<int:pk>/delete', PostDelete.as_view() ),
   path('category/<int:pk>/', CategorySubscribing.as_view(), name = 'category_nameurl'),

]