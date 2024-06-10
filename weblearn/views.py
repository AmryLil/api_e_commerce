# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic.base import TemplateView, View, RedirectView
# from seller.models import ListProduct


# class Card_con_cart(View):
#   template_name='base.html'
#   url = 'home'

#   def get(self, request, *args, **kwargs):
#     card_data = ListProduct.objects.get(id=kwargs['id'])
#     print(card_data.productname)
#     context={
#       'data' : card_data
#     }
#     return render(self.template_name, context ,request)
