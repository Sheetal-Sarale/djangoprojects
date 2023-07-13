from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
         abstract = True          # there is no any migration files are created


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=True)
    # created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name
    
# Extending usermodel
    # AbstractUser:  existing user model use karna hai and extra field add karna hai
    # AbstractBaseUser:existing user model ke field use nahi karna hai apko base se user model tayar karna hai
    # OnetoOneField:

    # inspectdb:

# Django Inheritance:

    # AbstractBaseClass Inhetitance:
    # MultiTableModel Inheritance: