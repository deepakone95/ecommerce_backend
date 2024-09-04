from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, CartViewSet,CatageoryViewSet, UserInfoViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'catageory', CatageoryViewSet)
router.register(r'userinfo', UserInfoViewSet)



urlpatterns = [
    path('',include(router.urls))

]