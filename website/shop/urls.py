from django.urls import path
from .views import main_home
from .views import main_shop

urlpatterns = [
    path('',main_home,name='main'),
    path('mag',main_shop,name='shop'),
]