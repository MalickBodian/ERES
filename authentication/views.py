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

@login_required(login_url="/")
def userList(request):
    users = Account.objects.filter(entite = request.user.entite)
    context = {'users':users}
    return render(request, 'accounts/userList.html', context)

@login_required(login_url="/")
def addUser(request):
    if request.method == "POST":
        data = {
            'email':request.POST.get('email', ''),
            'password1': request.POST.get('password1', ''),
            'password2': request.POST.get('password2', ''),
            'prenom': request.POST.get('prenom', ''),
            'nom':request.POST.get('nom', ''), 
            'adresse':request.POST.get('adresse', ''),
            'entite':request.user.entite,
            'tel':request.POST.get('tel', ''), 
            'role':request.POST.get('role', '')
        }
        # print(data['entite'])
        form = UserCreationForm2(data)
        if form.is_valid():
            form.save()
            # latest_id = Account.objects.latest('id').id
            # if request.user.id and latest_id:
            #     is_tracked = activity_tracker(request.user, latest_id, 'bala bala', 'ajouter', 'bd')
            #     print(is_tracked)
            is_new = True
            message = "l'utilisateur a été bien enrégistré"
            response = {
                'is_new': is_new,
                "message": message
            }
            response = json.dumps(response)

            return JsonResponse({"instance": response}, status=200)

        else:
            is_new = False
            message = "Oups!!! il y a une erreur veillez vérifiez les données soumisent svp"
            response = {
                'is_new': is_new,
                "message": message
            }
            response = json.dumps(response)

            return JsonResponse({"instance": response}, status=200)
    else:
        return render(request, 'accounts/addUser.html')

@login_required(login_url="/")
def updateUser(request, id=0):
    obj = get_object_or_404(Account, id=id)
    form = UpdateUserForm(request.POST or None, instance = obj)
    context= {'form': form}
    if form.is_valid():
        # form.instance.photo = request.FILES['image']
        form.save()
        return HttpResponseRedirect('/user/profile')
    else:
        context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)

@login_required(login_url="/")
def del_user(request, id):
    user = Account.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/user/liste-utilisateurs')

@login_required(login_url="/")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeFormEdit(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # if request.user.id:
            #     is_tracked = activity_tracker(request.user, 0, 'bala bala', 'modifier', 'bd')
            #     print(is_tracked)
            messages.success(request, 'Votre mot de passe a été modifier avec succés')
            return redirect('password')
        else:
            messages.error(request, 'SVP veillez corriger les erreurs ci aprés.')
    else:
        form = PasswordChangeFormEdit(request.user)
    return render(request, 'accounts/password.html', {
        'form': form
    })
