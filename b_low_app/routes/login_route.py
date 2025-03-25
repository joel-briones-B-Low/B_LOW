from django.shortcuts import render
import os

from ..forms import login_form

def login(request):
    if request.method == 'GET':
        
        return render(request, 'login.html',{
            'form': login_form
        })
    if request.method == 'POST':
        os.system('cls')
        print(request.POST)
        return render(request, 'login.html',{
            'form': login_form
        })
        