import datetime

from django.core.mail import mail_managers, EmailMultiAlternatives
from celery import shared_task
import time

from django.template.loader import render_to_string

from NewsPaper import settings
from news_paper.models import Post, Category


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

def send_mails():
    print('sending mail func')