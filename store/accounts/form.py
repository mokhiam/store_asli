from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from core.models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        Basket.objects.create(user=user)
        return user
