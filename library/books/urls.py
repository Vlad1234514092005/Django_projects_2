from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_main_page, name='show_main_page'),
    path('post/<int:pk>/', views.show_post_by_id, name='show_post_by_id'),
    path('post/add_book/', views.add_book, name='add_book'),
    path('post/<int:pk>/update_book/', views.update_book, name='update_book'),
    path('post/<int:pk>/delete_book/', views.delete_book, name='delete_book'),
]
