from django.urls import path
from .views import manage_books, register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('books/', manage_books, name='book'),
]
