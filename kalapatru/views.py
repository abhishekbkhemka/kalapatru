from django.http import JsonResponse
from django.shortcuts import redirect


def home(request):
    """API root — the UI lives on the Vite frontend (:5173)."""
    accept = request.headers.get('Accept', '')
    if 'text/html' in accept:
        return redirect('http://localhost:5173/')
    return JsonResponse({
        'service': 'kalapatru-api',
        'status': 'ok',
        'frontend': 'http://localhost:5173/',
        'admin': '/admin/',
        'auth': {
            'login': '/api/auth/login/',
            'me': '/api/auth/me/',
        },
    })
