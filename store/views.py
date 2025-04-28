from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Book, CartItem

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# ------------------- Book List View -------------------
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'store/book_list.html', {'books': books})


# ------------------- Add to Cart View -------------------
@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        return redirect('show_cart')


# ------------------- Show Cart View -------------------
class ShowCartView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


# ------------------- User Login View -------------------
class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('book_list')
        form = AuthenticationForm()
        return render(request, 'store/login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('book_list')

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book_list')
            else:
                messages.error(request, "Invalid credentials, please try again.")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('login')


# ------------------- Signup View -------------------
class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'store/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'store/signup.html', {'form': form})


# ------------------- Logout View -------------------
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
