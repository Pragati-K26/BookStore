from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.show_cart, name='show_cart'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.book_list, name='book_list'),
]