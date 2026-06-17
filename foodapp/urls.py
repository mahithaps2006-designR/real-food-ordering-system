from django.urls import path
from .views import *

urlpatterns = [

    path('', login_view, name='login'),

    path('register/', register_view, name='register'),

    path('hotels/', hotels_view, name='hotels'),
path(
    'menu/<int:hotel_id>/',
    menu_view,
    name='menu'
),path(
    'add-to-cart/<int:item_id>/',
    add_to_cart,
    name='add_to_cart'
),

path(
    'cart/',
    cart_view,
    name='cart'
),

path(
    'remove-cart/<int:cart_id>/',
    remove_cart_item,
    name='remove_cart'
),
path(
    'checkout/',
    checkout_view,
    name='checkout'
),
path(
    'payment/',
    payment_view,
    name='payment'
),

path(
    'order-success/<int:order_id>/',
    order_success_view,
    name='order_success'
),
path(
    'orders/',
    orders_view,
    name='orders'
),

]