from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length = 200)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    price = models.DecimalField(decimal_places = 2, max_digits = 50, default = 0.00)
    image = models.CharField(max_length = 1000)
    def get_price(self):
        return self.price
    
    def __str__(self):
        return self.group.name + " - " + self.name + " - " + str(self.price)
        
    def replacer(self):
        return self.name.replace(" ", "_")
        

