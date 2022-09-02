# В первую очередь мы импортируем библиотеку для работы с операционной системой и саму библиотеку Celery.
import os
from celery import Celery
# Второй строчкой мы связываем настройки Django с настройками Celery через переменную окружения.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final_project.settings')
# Далее мы создаём экземпляр приложения Celery,
app = Celery('Final_project')
# устанавливаем для него файл конфигурации. Мы также указываем пространство имён,
# чтобы Celery сам находил все необходимые настройки в общем конфигурационном файле settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Последней строчкой мы указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'email_weekly': {
        'task': 'news.tasks.celery_send_weekly_mail',
        'schedule': crontab(0, 12, day_of_week=[5])

     },
 }
