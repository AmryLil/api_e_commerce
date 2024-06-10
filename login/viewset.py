from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer, SignupSerializer
from rest_framework.authtoken.models import Token
from myaccount.serializers import ProfileSerializers
from myaccount.models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class LoginView(APIView):
    Current_User = None

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            self.Current_User = request.data['username']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            seller_group = Group.objects.get(name='seller')
            is_seller = seller_group in user.groups.all()
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)

                return Response(
                    {'message': 'Login berhasil!',
                     'username': user.username,
                     'email': user.email,
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'token' : token.key,
                     'is_seller':is_seller
                     
                     }
                    , status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Username atau password salah'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_current_user(self):
        return self.Current_User

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print(request.data)
            user=serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'message': 'Login berhasil!',
                     'username': user.username,
                     'email': user.email, 
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'token' : token.key
                     
                     }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
