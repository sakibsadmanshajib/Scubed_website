from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=64, default='Cash')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=3, default='BDT')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.CharField(max_length=64, default='Cash')
    type = models.CharField(max_length=8, default='debit')
    