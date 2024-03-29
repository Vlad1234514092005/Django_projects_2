from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_main_page, name='show_main_page'),
    path('post/<int:pk>/', views.show_post_by_id, name='show_post_by_id'),
]
