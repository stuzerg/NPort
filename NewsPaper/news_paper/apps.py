from django.apps import AppConfig


class NewsPaperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_paper'

    def ready(self):
        import news_paper.signals
        from .tasks import send_mails
        from .scheduler import rassylka_scheduler
        print('начало')

        # rassylka_scheduler.add_job(
        #     id='mail send',
        #     func=send_mails,
        #     trigger='interval',
        #     seconds=3,
        # )
        # rassylka_scheduler.start()
