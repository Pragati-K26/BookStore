from django.urls import path
from .views import (
    SignupView,
    UserLoginView,
    UserLogoutView,
    ShowCartView,
    AddToCartView,
    BookListView,
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('cart/', ShowCartView.as_view(), name='show_cart'),
    path('add_to_cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('', BookListView.as_view(), name='book_list'),
]
