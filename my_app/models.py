from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Work(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    postalZip = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.company


class Account(models.Model):
    pin = models.IntegerField()
    acc_num = models.CharField(max_length=50)
    pan = models.CharField(max_length=50)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_num


