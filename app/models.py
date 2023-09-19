from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    brand = models.CharField(max_length=40)
    taste = models.CharField(max_length=40)

class Parent_One(models.Model):
    first_name1 = models.CharField(max_length=40)
    surname1 = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name1

class Parent_Two(models.Model):
    first_name2 = models.CharField(max_length=40)
    surname2 = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name2

class Child(models.Model):
    first_parent = models.ForeignKey('Parent_One', on_delete=models.CASCADE)
    second_parent = models.ForeignKey('Parent_Two', on_delete=models.CASCADE)
    childs_first_name = models.CharField(max_length=40)
    childs_surname = models.CharField(max_length=40)