from django.contrib.auth.models import User
from django.db import models
import datetime

from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    def __str__(self):
     return f'{self.user.username}'



    def update_rating(self):
        s1 = s2 = s3 = 0

        r1 = Post.objects.filter(author=self).values('rating')          # множество всех лайков авторских постов
        s1 = sum([_['rating'] for _ in r1])
        s1 *= 3
        print('s1= ', s1)

        r2 = Comment.objects.filter(user=self.user).values('rating')    # множество всех лайков авторских комментариев
        s2 = sum([_['rating'] for _ in r2])
        print('s2= ', s2)


        r3 = Comment.objects.filter(post__author=self).values('rating') # множество всех лайков комментариев к статьям автора
        s3 = sum([_['rating'] for _ in r3])
        print('s3= ', s3)
        self.rating = s1 + s2 + s3
        self.save()
        print(f'рейтинг {self.user.username} обновлен. {self.rating}')





class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through="SubscribedCatUsers", )

    def __str__(self):
        return self.name


class Post(models.Model):
    type_choice = [('a', 'article'), ('n', 'news')]
    type_post = models.CharField(max_length=1, default='a', choices=type_choice)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    cat = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(default='нет заголовка', max_length=255)
    body = models.TextField(default='здесь ничего нет')
    rating = models.FloatField(default=1)

    def preview(self):
        # print(self.body[0:124]+'...')
        return self.body[0:124]+'...'

    @property
    def addit_prop(self):
        return "доп свойство"

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('post_create')
    # def __str__(self):
    #     return f'{self.header}, автор: {self.author}, тип:{self.type_post}'




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class SubscribedCatUsers(models.Model):
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_s = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='здесь ничего нет')
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)



    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


