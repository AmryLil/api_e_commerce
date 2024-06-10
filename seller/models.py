from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ListProduct(models.Model):
  productname   = models.CharField(max_length=255)
  brand         = models.CharField(max_length=255)
  category      = models.CharField(max_length=255)
  stock         = models.CharField(max_length=255)
  price         = models.CharField(max_length=255)
  image         = models.ImageField(upload_to='products/', blank=True, null=True)
  desc          = models.TextField(max_length=1000)
  seller        = models.CharField(max_length=255)
  

  def __str__(self):
    return self.productname
  

