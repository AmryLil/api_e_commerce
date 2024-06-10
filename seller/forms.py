# from django import forms
# from .models import ListProduct

# class addForms(forms.ModelForm):
#     class Meta:
#         model = ListProduct
#         fields = ['productname', 'brand', 'type', 'qty', 'price', 'image', 'desc']

#         TYPE_CHOICES = [
#             ('', ''),
#             ('Fashion', 'Fashion'),
#             ('Sport', 'Sport'),
#             ('Electronics', 'Electronics'),
#             ('Health and Beauty', 'Health and Beauty'),
#             ('Automotive', 'Automotive'),
#             ('Home and Garden', 'Home and Garden'),
#             ('Software and Apps', 'Software and Apps'),
#         ]

#         widgets = {
#             'productname': forms.TextInput(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm',
#                 'placeholder': 'product name'
#             }),
#             'brand': forms.TextInput(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm',
#                 'placeholder': 'enter brand'
#             }),
#             'type': forms.Select(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 pr-4 shadow-sm'
#             }, choices=TYPE_CHOICES), 
#             'qty': forms.NumberInput(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm',
#                 'placeholder': 'quantity your product'
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm',
#                 'placeholder': 'price'
#             }),
#             'image': forms.FileInput(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm'
#             }),
#             'desc': forms.Textarea(attrs={
#                 'class': 'mb-2 rounded-md py-1 px-2 shadow-sm',
#                 'placeholder': 'Enter your Description',
#                 'cols': '30',
#                 'rows': '4'
#             }),
#         }
