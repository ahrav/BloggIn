from django.urls import path

from .views import hello_world

url_patterns = [path("", hello_world, name="hello")]

