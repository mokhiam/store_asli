from django.contrib import admin
from .models import Categorie,Content,Basket

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('title','price','is_free')

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('title','description','image','price','is_free')

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display=('user','amounts')



