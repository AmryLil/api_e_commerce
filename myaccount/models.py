from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=255)
  shop_name = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  profile_picture = models.ImageField()

  def __str__(self) -> str:
    return self.username
  
  def save(self, *args, **kwargs):
        self.email = self.user.email
        if not self.name and self.user.first_name and self.user.last_name:
            self.name = f"{self.user.first_name} {self.user.last_name}"
        super(Profile, self).save(*args, **kwargs)


class DataSellers(models.Model):
    current_user =  models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255)
    delevery_service = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.shop_name
