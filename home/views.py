# from django.shortcuts import render, redirect
# from django.views.generic.base import RedirectView
# from django.urls import reverse_lazy
# from seller.models import ListProduct
# from django.contrib.auth import logout as logout_auth
# from django.contrib.auth.models import Group



# def logout(request):
#     logout_auth(request)
#     return redirect('home')

# def homePage(request):
#     card_data = None
#     context = {
#         'products': ListProduct.objects.all(),
#         'data_sports': ListProduct.objects.filter(type='Sport'),
#         'data': card_data,
#     }
#     return render(request, 'index.html', context)

# def FirstPage(request):
#     if request.user.is_authenticated:
#         firstname = request.user.first_name
#         lastname = request.user.last_name
#         username = firstname+" "+lastname
#     else :
#         username = "AnonymousUser"

    
#     print(username)
#     context={
#         'Username' : username
#     }
#     return render(request, 'firstpage.html', context)

# class Card_con_cart(RedirectView):
#     def get(self, request, *args, **kwargs):
#         card_id = kwargs.get('id')
#         if card_id:
#             try:
#                 card_data = ListProduct.objects.get(id=card_id)
#                 print(card_data.productname)
               
#             except ListProduct.DoesNotExist:
#                 pass
#         return super().get(request, *args, **kwargs)

#     def get_redirect_url(self, *args, **kwargs):
#         return reverse_lazy('home')



