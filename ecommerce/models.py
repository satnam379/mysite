from django.db import models



class Product(models.Model):
    productname = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.CharField(max_length=30)


    def __str__(self):
        return self.producttname

class Userss(models.Model):

    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    password = models.CharField(max_length=15)
    # orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return self.email


class Order(models.Model):

    products = models.ManyToManyField(Product)
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.products

