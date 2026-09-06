from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main"),
    path('service/<int:pk>/', service, name="service")
]