import datetime

from celery import shared_task
from django.contrib.auth.models import User

from django.core.mail import send_mail

from .models import Advertisement

"""
Теория по модулю Д10
@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

Здесь мы использовали функцию sleep() из пакета time, чтобы остановить выполнение процесса на 10 секунд. 
Это поможет нам убедиться, что Клиент не «встал», пока выполняется эта задача.
"""

@shared_task()
def celery_send_weekly_mail():
    from_date = datetime.datetime.now() - datetime.timedelta(days=7)
    recent_ads = Advertisement.objects.filter(creation_date__gte=from_date)
    sent_to_list = User.objects.values_list("email", flat=True)
    if recent_ads.exists():
        ads_count = recent_ads.count()
        send_mail(subject=f'Еженедельная рассылка',
                  message=f'Привет от сервиса "GoodGame! За эту неделю вышло {ads_count} новых новостей!',
                  from_email=None,
                  recipient_list=[sent_to_list])
