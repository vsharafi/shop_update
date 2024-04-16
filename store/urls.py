from django.urls import path
from .views import say_hello

urlpatterns = [
    path('<num>/', say_hello, name='hello'),
]