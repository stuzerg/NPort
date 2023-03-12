from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from NewsPaper import settings

from .models import PostCategory

def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview+'pk ='+str(pk),
            'link': f'http://127.0.0.1:8000/news/{pk}',
        }

    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.cat.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()
        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.header, subscribers)