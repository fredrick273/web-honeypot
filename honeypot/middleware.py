# middleware.py
import json
from .models import IntruderAction

class ActionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process each request
        response = self.get_response(request)

        # Extract IP address and user-agent
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # Log the action if accessing sensitive paths (like login, transfer, etc.)

        IntruderAction.objects.create(
            ip_address=ip_address,
            user_agent=user_agent,
            path=request.path,
            method=request.method,
            params=request.POST if request.method == 'POST' else None,
        )

        return response
