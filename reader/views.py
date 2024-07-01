

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from reader.models import Book
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'reader/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('book')
    else:
        form = UserLoginForm()
    return render(request, 'reader/login.html', {'form': form})

# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def manage_users(request):
#     users = User.objects.all()
#     return render(request, 'manage_users.html', {'users': users})

# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def create_book(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         Book.objects.create(name=name)
#         return redirect('manage_books')
#     return render(request, 'create_book.html')

@login_required
def manage_books(request):
    books = Book.objects.all()
    return render(request, 'reader/book_list.html', {'books': books})


