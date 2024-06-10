from rest_framework import serializers
from .models import Profile,DataSellers

class ProfileSerializers(serializers.HyperlinkedModelSerializer):
  class Meta :
    model = Profile
    fields = ['username','name','email','phone','shop_name','gender','date_of_birth','profile_picture']


class DataSellersSerializers(serializers.HyperlinkedModelSerializer):
  class Meta :
    model = DataSellers
    fields = ['current_user','shop_name','shop_address','delevery_service','email','phone']