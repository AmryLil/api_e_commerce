# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as login_auth,logout


# # Create your views here.
# def login(request):
#   if request.method=='POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')
        
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login_auth(request,user)
#       return redirect('first')
#     else:
#       return redirect('register')
#   return render(request,'login.html')

# def singup(request):
#   if request.method=='POST':
#     firstname = request.POST.get('firstname')
#     lastname = request.POST.get('lastname')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     confirm_password = request.POST.get('confirm_password')
#     if confirm_password != password :
#       return redirect('singup')
#     if User.objects.filter(username=username).exists() or User.objects.filter(email=email).    exists():
#       return redirect('singup')
   
#     User.objects.create_superuser(username=username, 
#                                   password=password, 
#                                   email=email, 
#                                   first_name=firstname, 
#                                   last_name=lastname)
#     user_login = authenticate(request, username=username, password=password)
#     login_auth(request, user_login)
#     return redirect('first')

#   return render(request,'singup.html')

# # def loginhandle(request):
#   if request.method=="POST":
#     USERNAME = request.POST['username']
#     PASSWORD = request.POST['password']
#     user = authenticate(request, username=USERNAME, password=PASSWORD)
#     print(user)
#     if user is not None:
#       login(request,user)
#       return redirect('first')
#     else:
#       return redirect('register')
    
#   return render(request,'login.html')
