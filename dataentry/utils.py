from django.apps import apps
from django.core.mail import EmailMessage
from django.conf import settings

def get_custom_models():
    default_models = ['LogEntry', 'Permission', 'Group', 'User', 'ContentType', 'Session', 'User', 'Upload']
    custom_models = []

    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)

    return custom_models


def send_mail_notification(mail_subject, message, to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
        mail.send()
    except Exception as e:
        raise e