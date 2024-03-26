from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_main_page, name='show_main_page')
]
