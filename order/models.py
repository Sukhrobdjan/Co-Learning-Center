from secrets import choice
from django.db import models
from helpers.models import BaseModel
from product.models import Product


NAQT = 'NAQT'
CARD = 'CARD'

CHOICES = [
    (NAQT, 'NAQT'),
    (CARD, 'CARD'),
    ]


class Basket(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.DecimalField(default=0)


class Order(BaseModel):
    phone_number = models.CharField(max_length=250)
    F_I_O = models.CharField(max_length=250)
    viloyat = models.CharField(max_length=250)
    tuman = models.CharField(max_length=250)
    aholi_punkti = models.TextField()
    manzil = models.TextField()
    job_location = models.TextField()


    basket = models.ForeignKey(Basket,on_delete=models.CASCADE)


    qushimcha = models.TextField()
    payment = models.CharField(max_length=9, choices=CHOICES)
