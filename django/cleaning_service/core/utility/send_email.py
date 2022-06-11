from django.core.mail import EmailMessage
from django.conf import settings


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(data['email_subject'], data['email_body'], settings.DEFAULT_FROM_EMAIL, [data['send_to'], ])

        email.send(fail_silently=False)
