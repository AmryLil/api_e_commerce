# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic.base import TemplateView, View, RedirectView
# from .models import ListProduct
# from .forms import addForms
# from django.contrib.auth.models import User


# class ProductList(TemplateView):
#   template_name = 'seller/index.html'
#   context={}
  
#   def get_context_data(self):
#     current_user = self.request.user.username
#     seller_user = User.objects.get(username=current_user)
#     self.context = {
#       'products' : ListProduct.objects.filter(seller=seller_user),
#       'data_sports' : ListProduct.objects.filter(type='Sport')
#     }
#     return self.context
  

# class AddProduct(View):
#   template_name = 'seller/add.html'
#   redirect_url = 'list'
#   context = {
#       'name':'Add Product',
#       'forms':addForms(),
#     }
  
#   def get(self, request, *args, **kwargs):
#     return render(request, self.template_name,self.context)
  
#   def post(self, request, *args, **kwargs):
#     addform = addForms(request.POST, request.FILES)
#     current_user = request.user.username
#     seller_user = User.objects.get(username=current_user)
#     if addform.is_valid() or request.method=='POST':
#       productname = addform.cleaned_data['productname'] 
#       brand = addform.cleaned_data['brand']
#       type = addform.cleaned_data['type']
#       qty = addform.cleaned_data['qty']
#       price = addform.cleaned_data['price']
#       imglink = addform.cleaned_data['image']
#       deks = addform.cleaned_data['desc']
      

#       ListProduct.objects.create(
#         productname   = productname,
#         brand         = brand,
#         type          = type,
#         qty           = qty,
#         price         = price,
#         desc          = deks,
#         image         = imglink,
#         seller        = seller_user
#       )
#       return redirect(self.redirect_url)
#     return render(request, self.template_name, self.context)

# class DeleteView(RedirectView):
#   def get_redirect_url(self,*args, **kwargs):
#     delete_id = kwargs['id']
#     print(delete_id)
#     ListProduct.objects.filter(id=delete_id).delete()
#     return reverse_lazy('list')

# class UpdateView(View):
#   template_name = 'seller/update.html'
#   form = addForms()
#   def get(self, request, *args, **kwargs):
#       update_data = ListProduct.objects.get(id=kwargs['id'])
#       data = update_data.__dict__
#       self.form = addForms(initial=data, instance=update_data)
#       context = {
#       'name':'Add Product',
#       'forms':self.form,
#       'id':update_data.id
#         }
#       return render(request, self.template_name, context)
  
#   def post(self, request, *args, **kwargs):
#       update_data = ListProduct.objects.get(id=kwargs['id'])
#       self.form = addForms(request.POST, instance=update_data)
#       context = {
#       'name':'Add Product',
#       'forms':self.form,
#       'id':update_data.id
#         }
#       if self.form.is_valid() or request.method=='POST':
#         self.form.save()
#         return redirect('list')
#       return render(request, self.template_name, context)

    




