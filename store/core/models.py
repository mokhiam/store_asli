from django.db import models
from accounts.models import User

class Basket(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amounts=models.IntegerField(default=0)

class Categorie(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    is_free=models.BooleanField(default=False)
    baskets=models.ManyToManyField(Basket,null=True,blank=True)

class Content(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField()
    price=models.IntegerField()
    is_free=models.BooleanField(default=False)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    baskets=models.ManyToManyField(Basket,null=True,blank=True)

class Credit_charge(models.Model):
    cardnumber=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    cv2=models.CharField(max_length=5)






