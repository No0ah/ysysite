from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': '欢迎使用 Django REST API',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
        }
    })
