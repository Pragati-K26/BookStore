from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, CartItem

def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('show_cart')

@login_required
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('book_list')
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
