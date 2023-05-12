from django.db import models

# Create your models here.
from django.db import models
from datetime import date
# Create your models here.

class Rentage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='rentage', null=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


FUEL= (
    ('petrol', 'petrol'),
    ('diesel', 'diesel')
)

class Brand(models.Model):
    category =  models.ForeignKey(Rentage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand', null=True)
    description = models.TextField( max_length=255)
    discount = models.PositiveIntegerField( null=True, default=0, blank=True )
    amount = models.IntegerField(null=True)
    inventory  = models.PositiveIntegerField()
    created_at  = models.DateField( auto_now_add= True)
    fuel = models.CharField(max_length=50, choices=FUEL, null=True)
    capacity = models.CharField(max_length=50, null=True)
    




    def __str__(self) ->str:
        return self.title

   
ORDER_STATUS=(
    ('Pending', 'Pending'),
    ('Cancel Payment','Cancel Payment' ),
    ('Payment Received','Payment Received'),
    ('Order in progress', 'Order in progress'),
    ('Order Received','Order Received'),
)


PAYMENT_METHOD=(
    ('Paystack','Paystack'),
    ('Transfer', 'Transfer')
)
 





class Order(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    surname= models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255, null=True)
    middlename = models.CharField(max_length=255, null=True)
    address  = models.TextField()
    email= models.EmailField(max_length=255)
    phone = models.CharField(max_length=50)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default='pending')
    date_of_birth = models.DateTimeField(blank=True, null=True)
    booking = models.DateField(blank=True, null=True)
    returnbooking = models.DateField(blank=True, null=True)
    # total_days  = models.IntegerField(null=True, blank=True)
    
    # total_amount = models.IntegerField(blank=True, null=True)
    isAvailable = models.BooleanField(default=True)    
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, default='paystack')
    ref = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) ->str:
        return self.middlename

    @property
    def getnumdays(self):
        dif =(self.returnbooking - self.booking).days
        return dif
    
    @property
    def gettotalamount(self):
        amount= self.brand.amount
        total_amount = ((self.returnbooking - self.booking).days) * amount
        return total_amount
        