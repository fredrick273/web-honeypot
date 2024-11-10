# signals.py
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from .models import IntruderAction

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Log failed login attempt
    IntruderAction.objects.create(
        ip_address=ip_address,
        user_agent=user_agent,
        path=request.path,
        method=request.method,
        params={'username': credentials.get('username')},
    )
