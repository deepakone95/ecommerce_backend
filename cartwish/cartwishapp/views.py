from django.shortcuts import render
from rest_framework import viewsets
from .models import Products, Orders, UserInfo, Cart, Catageory
from .serializers import ProductSerializer,OrderSerializer,CartSerializer, CatageorySerializer, UserInfoSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CatageoryViewSet(viewsets.ModelViewSet):
    queryset = Catageory.objects.all()
    serializer_class = CatageorySerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer