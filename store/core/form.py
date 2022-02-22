from rest_framework import serializers
from .models import Credit_charge

class Credit_charge_Form(serializers.ModelSerializer):
    class Meta:
        model=Credit_charge
        fields=('cardnumber','password','cv2')
        
