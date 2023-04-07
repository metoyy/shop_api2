from celery import shared_task
from account.send_mail import send_confirmation_email
from .celery import app as CeleryApp


@CeleryApp.task
def send_confirm_email_task(user, code):
    send_confirmation_email(user, code)

