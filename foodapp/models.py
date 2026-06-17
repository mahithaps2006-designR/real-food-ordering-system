from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='hotels/')

    def __str__(self):
        return self.name
class MenuItem(models.Model):

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='menu/'
    )

    def __str__(self):
        return self.name
class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        default=1
    )

    def __str__(self):
        return self.user.username
class Customer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.full_name




class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=50
    )

    status = models.CharField(
        max_length=30,
        default='Ordered'
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.id}"

    class Order(models.Model):
        user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )

        customer = models.ForeignKey(
            Customer,
            on_delete=models.CASCADE
        )

        total_amount = models.DecimalField(
            max_digits=10,
            decimal_places=2
        )

        payment_method = models.CharField(
            max_length=50
        )

        status = models.CharField(
            max_length=30,
            default='Ordered'
        )

        order_date = models.DateTimeField(
            auto_now_add=True
        )

        def __str__(self):
            return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return self.menu_item.name
