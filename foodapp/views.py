from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import (Hotel, MenuItem, Cart,Customer,Order,
    OrderItem)
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('hotels')

        else:

            return render(
                request,
                'login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(request, 'login.html')
def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')
def hotels_view(request):

    hotels = Hotel.objects.all()

    return render(
        request,
        'hotels.html',
        {'hotels': hotels}
    )
def menu_view(request, hotel_id):

    hotel = Hotel.objects.get(id=hotel_id)

    menu_items = MenuItem.objects.filter(
        hotel=hotel
    )

    return render(
        request,
        'menu.html',
        {
            'hotel': hotel,
            'menu_items': menu_items
        }
    )
def add_to_cart(request, item_id):

    item = MenuItem.objects.get(
        id=item_id
    )

    cart_item = Cart.objects.filter(
        user=request.user,
        menu_item=item
    ).first()

    if cart_item:

        cart_item.quantity += 1

        cart_item.save()

    else:

        Cart.objects.create(
            user=request.user,
            menu_item=item,
            quantity=1
        )

    return redirect('cart')
def cart_view(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:

        total += (
            item.menu_item.price *
            item.quantity
        )

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
def remove_cart_item(request, cart_id):

    item = Cart.objects.get(
        id=cart_id
    )

    item.delete()

    return redirect('cart')
def checkout_view(request):

    if request.method == 'POST':

        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']

        Customer.objects.update_or_create(
            user=request.user,
            defaults={
                'full_name': full_name,
                'phone': phone,
                'address': address,
                'city': city,
                'pincode': pincode
            }
        )

        return redirect('payment')

    customer = Customer.objects.filter(
        user=request.user
    ).first()

    return render(
        request,
        'checkout.html',
        {'customer': customer}
    )
def payment_view(request):

    customer = Customer.objects.get(
        user=request.user
    )

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:

        total += (
            item.menu_item.price *
            item.quantity
        )

    if request.method == 'POST':

        payment_method = request.POST[
            'payment_method'
        ]

        order = Order.objects.create(
            user=request.user,
            customer=customer,
            total_amount=total,
            payment_method=payment_method
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                menu_item=item.menu_item,
                quantity=item.quantity,
                price=item.menu_item.price
            )

        cart_items.delete()

        return redirect(
            'order_success',
            order.id
        )

    return render(
        request,
        'payment.html',
        {
            'total': total,
            'customer': customer
        }
    )
def order_success_view(
    request,
    order_id
):

    order = Order.objects.get(
        id=order_id
    )

    return render(
        request,
        'order_success.html',
        {'order': order}
    )
def orders_view(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-order_date')

    return render(
        request,
        'orders.html',
        {'orders': orders}
    )