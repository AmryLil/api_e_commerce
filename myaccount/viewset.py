from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile,DataSellers
from .serializers import DataSellersSerializers,ProfileSerializers
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class ProfileAPIView(APIView):
    def post(self, request, format=None):
        user = request.user  # Mendapatkan pengguna yang sedang login

        # Cek jika profil pengguna sudah ada
        try:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializers(profile, data=request.data)
        except Profile.DoesNotExist:
            serializer = ProfileSerializers(data=request.data)

        if serializer.is_valid():
            # Simpan profil pengguna
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataSellersAPIView(APIView):
    def post (self, request):
        serializer = DataSellersSerializers(data=request.data)
        UserName = request.data['current_user']
        current_user = User.objects.get(username=UserName)
        seller_group = Group.objects.get(name='seller')
        print("anu")
        if serializer.is_valid():
            is_seller = seller_group.user_set.filter(id=current_user.id).exists()
            print(is_seller)
            if not is_seller :
                seller_group.user_set.add(current_user)
            data_seller=serializer.save()
            return Response(
                {
                'current_user' : UserName,
                'shop_name':data_seller.shop_name,
                'shop_address':data_seller.shop_address,
                'delevery_service':data_seller.delevery_service,
                'email':data_seller.email,
                'phone':data_seller.phone,
                'is_seller':is_seller
                },status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
