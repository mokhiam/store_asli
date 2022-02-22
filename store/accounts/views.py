from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from .models import *
from .form import SignUpForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!',status=200)

        return HttpResponse(f"{form.errors}") 

    return HttpResponse('Only post method allowed!')
        
