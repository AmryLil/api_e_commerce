from django.urls import path, include
# from .views import ProductList,DeleteView,UpdateView
from .viewset import ProductViewSeller,AllProductView,UpdateProduct,DeleteProduct,AddProduct

urlpatterns=[
  # path('', ProductList.as_view(), name='list'),
  # # path('addproduct/', AddProduct.as_view(), name='add'),
  # path('delete/<int:id>/', DeleteView.as_view(), name='delete'),
  # path('update/<int:id>', UpdateView.as_view(), name='update'),

  path('api/product', AllProductView.as_view(), name='product'),
  path('api/myproduct', ProductViewSeller.as_view(), name='myproduct'),
  path('api/addproduct', AddProduct.as_view(), name='addproduct'),
  path('api/updateproduct/<int:id>/', UpdateProduct.as_view(), name='updateproduct'),
  path('api/deleteproduct/<int:id>/', DeleteProduct.as_view(), name='deleteproduct'),
]