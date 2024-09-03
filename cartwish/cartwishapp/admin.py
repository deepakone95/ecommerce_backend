from django.contrib import admin
from .models import Cart,Orders,Products,Catageory, UserInfo
# Register your models here.

admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(Catageory)
admin.site.register(UserInfo)
