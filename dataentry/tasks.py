from main.celery import app
import time
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_mail_notification

@app.task
def celery_test_task():
    time.sleep(10)
    # send an email
    message = 'Test email with celery'
    mail_subject = 'Test subject'
    to_email = settings.DEFAULT_TO_EMAIL
    send_mail_notification(mail_subject, message, to_email)
    return 'Email sent'

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
        messages.success(request, 'Data imported successfully!')
    except Exception as e:
        raise e
    
    message = 'Data imported successfully'
    mail_subject = ' Data import completed.'
    to_email = settings.DEFAULT_TO_EMAIL
    send_mail_notification(mail_subject, message, to_email)