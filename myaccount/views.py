from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

# Create your views here.
def baseview(request):

    url = None
    name = None
    if request.user.groups.filter(name='seller').exists():
            url = 'list'
            name = "My Product"
    else :
        url = 'selleraccount'
        name = 'Create Seller Account'

    context = {
        'url_name' : url,
        'name': name
    }   
    return render(request, "basehome.html", context)


def profileView(request):
    return render(request, "profile.html")

def CreateSellerAccountView(request):

    
    seller_group = Group.objects.get(name='seller')
    if request.user.is_authenticated:
        if request.method=='POST':
            current_user = request.user
            seller_group.user_set.add(current_user)
            return redirect('selleraccount')
        
        
    else :
        return redirect('register') 

    return render(request, "create_seller.html")

