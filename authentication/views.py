from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
import os
from django.http import JsonResponse, response
import json


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                msg = 'Mot de passe et/ou Identifiant invalides :('
        else:
            msg = 'Oups une erreur s\'est produite!!!'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('login')

@login_required(login_url="/")
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required(login_url="/")
def editPhoto(request, id):
    obj = get_object_or_404(Account, id=id)
    form = UpdateUserForm(request.POST or None, instance = obj)
    context= {'form': form}
    if form.is_valid():
        form.instance.photo = request.FILES['image']
        form.save()
        return HttpResponseRedirect('/profile')
    else:
        context = {'form': form}
    return render(request, 'accounts/edit_photo.html', context)







