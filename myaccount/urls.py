from django.urls import path
from . import views
from .viewset import DataSellersAPIView

urlpatterns=[
  path('',views.profileView, name='myaccount'),
  path('createselleraccount/',views.CreateSellerAccountView, name='selleraccount'),
  path('api/data-seller',DataSellersAPIView.as_view(), name='api-data-seller')
]