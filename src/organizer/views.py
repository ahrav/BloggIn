from django.http import HttpResponse
from django.views.decorator.http import require_http_methods


@require_http_methods(["GET", "HEAD"])
def hello_world(request):
    return HttpResponse("Hello World!")
