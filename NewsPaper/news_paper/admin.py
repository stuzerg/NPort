
from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['body', 'type_post', "addit_prop"] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('cat', 'type_post')
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
# Register your models here.
