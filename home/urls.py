from django.urls import path
from . import views

urlpatterns=[
  path('',views.FirstPage, name='first'),
  path('home/',views.homePage, name='home'),
  path('logout/',views.logout, name='logout'),
  path('cardcart/<int:id>', views.Card_con_cart.as_view(), name='cardcart')
]