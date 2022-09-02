from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from Final_project.advertisements.models import Feedback

@receiver(post_save, sender=Feedback)
def notify_feedback_maker(sender, instance, created, **kwargs):
    if created == False:
        instance.feedback.save()
        print("реакция")
        html_content = render_to_string('email/react_to_feedback_mail.html', {'feedback_save': instance}, )
        email_of_author = instance.author.email
        sendto = email_of_author
        print("реакция")
        # формируем список для рассылки
        """
        msg = EmailMultiAlternatives(
            subject=f'"Здравствуйте, {instance.author.user} Новая реацкия на ваш отклик!"',
            body=f'Пользователь {instance.ad.user} принял ваш отклик: {instance.text} на его объявление',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=sendto)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        """