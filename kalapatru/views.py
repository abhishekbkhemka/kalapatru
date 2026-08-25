import os

from django.http import JsonResponse
from django.shortcuts import redirect


def home(request):
    """API root health/info. Never hardcode localhost in production."""
    frontend = os.environ.get('FRONTEND_URL', '').rstrip('/')
    payload = {
        'service': 'kalapatru-api',
        'status': 'ok',
        'admin': '/admin/',
        'auth': {
            'login': '/api/auth/login/',
            'me': '/api/auth/me/',
        },
    }
    if frontend:
        payload['frontend'] = frontend

    accept = request.headers.get('Accept', '')
    if 'text/html' in accept and frontend:
        return redirect(frontend + '/')
    return JsonResponse(payload)
