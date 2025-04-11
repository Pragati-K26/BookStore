from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, CartItem
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1  # Increase quantity if item already exists
    cart_item.save()
    return redirect('show_cart')

@login_required
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('book_list')  # If the user is already logged in, redirect them to the book list

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book_list')  # Redirect to the book list after login
            else:
                messages.error(request, "Invalid credentials, please try again.")
                return redirect('login')  # Stay on login page if authentication fails
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('login')  # Stay on login page if the form is not valid

    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'store/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
