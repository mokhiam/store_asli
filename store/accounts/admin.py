from django.contrib import admin
from .models import User
from core.models import *

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=('username','password','balance','basket_amount')
    def basket_amount(self,obj):
        return obj.basket.amounts


