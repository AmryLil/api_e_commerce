from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListProduct
from .serializers import ProductsSerializers
from login.viewset import LoginView
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view


class AllProductView(APIView):
    def get(self,request):
        queryset = ListProduct.objects.all()
        serializer = ProductsSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductViewSeller(APIView):
    def get(self, request):
        user_login = LoginView()
        current_user = user_login.get_current_user()
        print(current_user)

        if current_user is None :
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        else :
            if current_user.is_authenticated:
                queryset = ListProduct.objects.filter(seller=current_user)
                serializer = ProductsSerializers(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

class AddProduct(APIView):
    parser_classes = [MultiPartParser]
    def post(self,request):
        serializer = ProductsSerializers(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProduct(APIView):
    def patch (self,request,id):
        try:
            queryset = ListProduct.objects.get(id=id)
        except ListProduct.DoesNotExist:
            return Response({'message':"Data Tidak Ditemukan"},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsSerializers(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class DeleteProduct(APIView):
    def delete(self,request,id):
        try:
            queryset = ListProduct.objects.get(id=id)
        except ListProduct.DoesNotExist:
            return Response({'message':"Data Tidak Ditemukan"},status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'message':'Data berhasil dihapus'},status=status.HTTP_204_NO_CONTENT)
  
        
            