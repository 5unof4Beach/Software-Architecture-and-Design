from __future__ import unicode_literals
from django.db import models

class Author(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField.primary_key
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    created_at = models.DateField
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.name)
    
class Publisher(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateField
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.name)    
    
class Category(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateField
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.name)

# This is our model for user registration.
class Book(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField.primary_key
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    published_at = models.DateField
    created_at = models.DateField
    updated_at = models.DateField
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.id)
    
# Customer Service

class Account(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField.primary_key
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.username)
    
class Address(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField.primary_key
    address = models.CharField(max_length=255)
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.address)
    
class Fullname(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField.primary_key
    fullname = models.CharField(max_length=255)
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.name)

class Customer(models.Model):
    ### The following are the fields of our table.
    id = models.IntegerField
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE)
    fullnameID = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    addressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    ### It will help to print the values.
    def __str__(self):
        return '%s' % (self.name)
