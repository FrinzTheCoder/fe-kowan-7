from django.urls import path

from fe.views import *

app_name = 'fe'

urlpatterns = [
    path('', home, name='home'),
    path('proxy/square/', proxy_square, name='proxy_square'),
    path('proxy/cube/', proxy_cube, name='proxy_cube'),
]