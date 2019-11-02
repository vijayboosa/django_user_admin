from django.urls import path

from .views import test_app_view

urlpatterns = [
    path('', test_app_view, name='testapphome'),
]
