from rest_framework.views import APIView
from rest_framework.response import Response
from .form import Credit_charge_Form
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class Charge(APIView):
    # permission_classes=(IsAuthenticated,)
    def post(self,request,*args, **kwargs):
        pypl=Credit_charge_Form(data=request.data)
        if pypl.is_valid():
            pypl.save()
            request.user.balance+=kwargs['amount']
            request.user.save()
            return Response({'message': 'Charge successfully!'},status=200)
        return Response({'message': pypl.errors})
    def get(self,request):
        return Response('Please login with post method')


class Buy(APIView):
    # permission_classes=(IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        user=User.objects.get(username=request.user.username)
        return Response({'message': str(request.user.username)},status=200)
        if kwargs['quality']=='Categorie':
            cat=Categorie.objects.get(id=kwargs['quality_id'])
            cat.baskets.add(user.basket)
            user.basket.amounts+=cat.price
            return Response({'message': 'categorie add!'},status=200)
        elif kwargs['quality']=='Content':
            con=Content.objects.get(id=kwargs['quality_id'],)
            con.baskets.add(user.basket)
            user.basket.amounts+=con.price
            return Response({'message': 'content add!'},status=200)
    def get(self,request):
        return Response('Please login with post method')
    
            
        


