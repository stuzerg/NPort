import datetime

from django.core.mail import mail_managers, EmailMultiAlternatives
from celery import shared_task
import time

from django.template.loader import render_to_string

from NewsPaper import settings
from news_paper.models import Post, Category, PostCategory, SubscribedCatUsers




# @shared_task
# def hello():
#     time.sleep(3)
#     print("Hello, world!")

@shared_task
def spamming(slovo):
    print(slovo)
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)

    posts = Post.objects.filter(creation_date__gte=last_week)

    categories = set(posts.values_list('cat__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    subscribers.remove('')
    subscribers.remove(None)
    print(f'subscribers weekly list = {subscribers}')
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,

        }

    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    return "spamming succeed"

@shared_task
def send_notify(pk):

    messag = 'вход в таску, pk = '+ str(pk)
    print(messag)

    pst = Post.objects.get(pk=pk)
    categories = set(PostCategory.objects.filter(post=pst).values_list('category', flat=True))
    subscribers = set(SubscribedCatUsers.objects.filter(categ_id__in=categories).values_list('user_s__email', flat=True))

    try:
        subscribers.remove('')
    except:
        pass
    try:
        subscribers.remove(None)
    except:
        pass

    kate = [Category.objects.get(pk=k).name for k in categories ]

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': pst.preview,
            'link': f'http://127.0.0.1:8000/news/{pk}',
              'kate' : kate,
        }

    )

    msg = EmailMultiAlternatives(
        subject=pst.header,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    return     (f'subscribers weekly list = {subscribers}','categories are: ',kate)


def send_mails():
    print('sending mail func')