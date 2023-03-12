# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
import http.client
from datetime import datetime

import requests
from django.core.mail import EmailMultiAlternatives
from django.forms import *
from django.http import HttpResponse, request

from django.shortcuts import render, redirect
from django.template import context
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .filters import PostFilter
from .forms import PostForm #, CategoryForm
from .models import Post, Category, PostCategory, Author, SubscribedCatUsers
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostNewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post

    queryset = Post.objects.filter(type_post = 'n').order_by('-creation_date')

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 3

class PostArticlesList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    #model = Post

    queryset = Post.objects.filter(type_post = 'a').order_by('-creation_date')

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 3
class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    #model = Post

    queryset = Post.objects.all().order_by('-creation_date')

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 3
class PostListFiltered(ListView):
    # Указываем модель, объекты которой мы будем выводить
    #model = Post

    queryset = Post.objects.all().order_by('-creation_date')

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts_filtered.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 3


    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict

        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)

        # Возвращаем из функции отфильтрованный список
        return self.filterset.qs




class PostDetail(DetailView):

    model =Post

    # model.cat_list = Category.PostCategory.objects.filter(post_id =1)
    template_name = 'post.html'

    context_object_name = 'post'

    def get_context_data(self, **kwargs):

       context = super().get_context_data(**kwargs)
       _pk =context['object']
       context['categ'] = str((PostCategory.objects.filter(post = Post.objects.get(pk = 1))).values_list('category')[0])

       return context



class PostCreate(PermissionRequiredMixin, CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm

    # модель
    model = Post
    permission_required = ('news_paper.add_post',)
    # и новый шаблон, в котором используется форма.
    template_name = 'post_a_edit.html'

    def form_valid(self, form):
        pst = form.save(commit=False)
        if ('news' in self.request.path):
            pst.type_post = 'n'
        if ('articles' in self.request.path):
            pst.type_post = 'a'
        pst = form.save(commit=True)
        kate = PostCategory.objects.filter(post = pst )
        for k in kate:
            print ("cat =", k.category.name)
            subs_list = SubscribedCatUsers.objects.filter(categ = k.category)
            # email_lst = []
            for sub in subs_list:
                print(sub.user_s.email)
                html_content = render_to_string(
                    'subscription_registered.html',
                    {
                        'post': pst,
                        'k' : k,
                        'sub' :sub
                    }
                )
                # print(html_content)
                if sub.user_s.email != '':
                    msg = EmailMultiAlternatives(
                        subject=pst.header,
                        body="",
                        from_email='stutzerg@yandex.ru',
                        to=[sub.user_s.email],
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()


        return super().form_valid(form)


    success_url = reverse_lazy('post_list')



class PostEdit(PermissionRequiredMixin, UpdateView):
        form_class = PostForm
        model = Post
        permission_required = ('news_paper.change_post',)
        Post.wrong_state = False
        template_name = 'post_a_edit.html'
        def __init__(self):
            Post.wrong_state = False

        def form_valid(self, form):
            curr = form.save(commit=False)
            if (curr.type_post == 'a' and 'news' in self.request.path) or \
                    (curr.type_post == 'n' and 'articles' in self.request.path):

                Post.wrong_state = True
                return self.form_invalid(form)
            else:
                Post.wrong_state = False


            return super().form_valid(form)





class PostDelete(PermissionRequiredMixin, DeleteView):


    model = Post
    permission_required = ('news_paper.change_post',)

    template_name = 'post_delete.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        if   ('articles' in (self.request.path) and (context.get('post').type_post) == 'a') \
                or ('news' in (self.request.path) and (context.get('post').type_post) == 'n'):

            pass

        else:
            raise http.client.error('Ошибка типизации при УДАЛЕНИИ поста (статья/новость)')





        return context



    success_url = reverse_lazy('post_list')

class CategorySubscribing(DetailView):

    model = Category
    # form_class = CategoryForm


    template_name = 'categoryhtml.html'
    context_object_name = 'categ_context'
    val = 'some01'
    def get_context_data(self, **kwargs):

        tag = kwargs
        context = super().get_context_data(**kwargs)
        context['messag'] = self.val





        return context




    def post(self, request, *args, **kwargs):
        self.context_object_name = 'categ_context'
        user=request.user
        tag = kwargs["pk"]

        if not (SubscribedCatUsers.objects.filter(user_s=user, categ = tag).exists()):
             sub_user = SubscribedCatUsers(user_s=user, categ = Category(pk = tag))
             sub_user.save()
             resp = HttpResponse('you have a new subscription')

             return resp




        return  HttpResponse('you already have this subscription', tag)