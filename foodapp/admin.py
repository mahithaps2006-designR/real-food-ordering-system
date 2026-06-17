from django.contrib import admin
from .models import (Hotel, MenuItem, Cart,
    Customer,Order,
    OrderItem)

admin.site.register(Hotel)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)