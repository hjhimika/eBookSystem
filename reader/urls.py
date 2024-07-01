from django.urls import path
from .views import manage_books, register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    # path('manage-users/', manage_users, name='manage_users'),
    # path('create-book/', create_book, name='create_book'),
    path('books/', manage_books, name='book'),
]
