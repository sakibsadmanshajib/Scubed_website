from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, default='Cash')
    description = models.CharField(max_length=512, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    currency = models.CharField(max_length=4, default='BDT')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.CharField(max_length=128, primary_key=True, blank=True, unique=True, default=uuid.uuid4)
    user = models.CharField(max_length=128, default='Anonymous')
    timestamp = models.DateTimeField(default=timezone.now())
    account = models.CharField(max_length=128, default='Cash')
    type = models.CharField(max_length=8, default='debit')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    remark = models.CharField(max_length=256)

    def __str__(self):
        return self.id

class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_transaction = models.CharField(max_length=128, default='none')
    total_debit = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total_credit = models.DecimalField(max_digits=20, decimal_places=2, default=0)