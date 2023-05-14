from django.urls import path
from .views import *

urlpatterns = [
    path('', get_home, name='home'),
    path('about/', get_about, name='about'),
    path('service/', get_service, name='service'),
    path('menu/', get_menu, name='menu'),
    path('contact/', get_contact, name='contact'),
]