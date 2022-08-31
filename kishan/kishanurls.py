from django.urls import path

from kishan.views import kishanmethod

urlpatterns = [
    path('hello/', kishanmethod),   #app hitting end point --> method name
]