# from multiprocessing import context
from django.shortcuts import render, redirect
from requests import request
from .forms import *
from .models import *
from django.urls import reverse
from django.shortcuts import redirect
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from .forms import *


@login_required(login_url="/")
def index(request):
    context = {'segment': 'index'}
    return render(request,"home/index.html", context)

############################### CRUD de la table Patients ########################################
@login_required(login_url="/")
def patient(request):
    context = {
        'patients' : Patients.objects.filter(entite = request.user.entite)
    }
    return render(request, 'home/patients.html', context)

@login_required(login_url="/")
def addPatient(request):
    context = {
        'docteurs':Account.objects.filter(entite = request.user.entite)
    }
    if request.method == 'POST':
        if request.POST.get('prenom') and request.POST.get('nom') and request.POST.get('adresse') and request.POST.get('tel') and request.POST.get('date') and request.POST.get('age') and request.POST.get('medecin') and request.POST.get('gs') and request.POST.get('proffession') and request.POST.get('sex'):
            medecin = Account.objects.get(id=request.POST['medecin'])

            proto = Patients()
            proto.prenom = request.POST.get('prenom')
            proto.nom = request.POST.get('nom')
            proto.adresse = request.POST.get('adresse')
            proto.tel = request.POST.get('tel')
            proto.dateNaissance = request.POST.get('date')
            proto.age = request.POST.get('age')
            proto.entite = request.user.entite
            proto.docteur = medecin
            proto.groupSanguin = request.POST.get('gs')
            proto.proffesion = request.POST.get('proffession')
            proto.sexe = request.POST.get('sex')
            # try:
            proto.save()
            # except:
            return HttpResponseRedirect('/home/patients')
    return render(request, 'home/ajoutPatient.html', context)#{'form':form, 'submitted':submitted})


# @login_required(login_url="/")
# def editPatient(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = PatientForm()
#         else:
#             traitement = Patients.objects.get(pk=id)
#             form = PatientForm(instance=traitement) 
#         return render(request, "home/ajoutPatient.html", {'form':form})
#     else:
#         if id == 0:
#             form = PatientForm(request.POST)
#         else:
#             traitement = Patients.objects.get(pk=id)
#             form = PatientForm(request.POST, instance = traitement)
#         if form.is_valid():
#             form.save()
#         return redirect('/patients')

# def patientDelete(request, id):
#     employee = Patients.objects.get(pk=id)
#     employee.delete()
#     return redirect('/home/patients')


############################### Informations générales du patient ########################################
@login_required(login_url="/")
def DetailPatient(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    antecedents = Antecedant.objects.filter(patient = obj)
    if request.method == 'POST':
        form = AntecedantForm(request.POST)
        if form.is_valid():
            form.instance.patient = obj
            form.save()
    else:
        form = AntecedantForm
        if 'submitted' in request.GET:
            submitted = True
    form = AntecedantForm
    context = {
        'detail':obj,
        'antecedents':antecedents,
        'form':form
    }
    return render(request, 'home/detail-patient.html', context)

# @login_required(login_url="/")
# def addAntecedant(request, id=0):
#     submitted = False
#     obj = get_object_or_404(Patients, id=id)
#     if request.method == 'POST':
#         form = AntecedantForm(request.POST)
#         if form.is_valid():
#             form.instance.patient = obj
#             form.save()
#     else:
#         form = AntecedantForm
#         if 'submitted' in request.GET:
#             submitted = True
#     form = AntecedantForm
#     return render(request, 'home/add_employee.html', {'form':form, 'submitted':submitted})




############################### CRUD de la table DossierPatient ########################################
@login_required(login_url="/")
def dossier(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    context = {
        'dossier':obj,
        'dossierPatient':DossierPatient.objects.filter(patient = obj)
    }
    return render(request, 'home/dossierPatient.html', context)

@login_required(login_url="/")
def addDossier(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    submitted = False
    if request.method == 'POST':
        form = AjoutdossierForm(request.POST)
        if form.is_valid():
            form.instance.patient = obj
            form.instance.entite = request.user.entite
            form.save()
            return redirect('dossier', id)
    else:
        form = AjoutdossierForm
        if 'submitted' in request.GET:
            submitted = True
    form = AjoutdossierForm
    context = {
        'ajout':obj,
        'form':form
    }
    return render(request, 'home/ajoutDossier.html', context)

@login_required(login_url="/")
def editDossier(request, pk=0, id=0):
    patient = get_object_or_404(Patients, pk=pk)
    obj = get_object_or_404(DossierPatient, id=id)
    form = AjoutdossierForm(request.POST or None, instance = obj)
    context= {'form': form}
    if form.is_valid():
        form.save()
        return redirect('dossier', pk)
    else:
        context = {'form': form}
    return render(request, 'home/ajoutDossier.html', context)

@login_required(login_url="/")
def delDossier(request, pk, id):
    patient = get_object_or_404(Patients, pk=pk)
    dossier = DossierPatient.objects.get(pk=id)
    dossier.delete()
    return redirect('dossier', pk)

############################### CRUD de la table Radio ########################################
@login_required(login_url="/")
def radioList(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    radios = Radio.objects.filter(patient = obj).order_by('-id')
    context = {
        'obj':obj,
        'radios':radios
    }

    return render(request, 'home/radio.html', context)

@login_required(login_url="/")
def viewRadio(request, pk=0, id=0):
    patient = get_object_or_404(Patients, pk=pk)
    radio = get_object_or_404(Radio, id=id)
    context = {'obj':radio, 'patient':patient}

    return render(request, 'home/viewRadio.html', context)

@login_required(login_url="/")
def radioAdd(request, id):
    obj = get_object_or_404(Patients, id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        radio = Radio()
        radio.patient = obj
        radio.photo = request.FILES['image']
        radio.save()
        return redirect('radio', id)
    else:
        context = {'obj':obj}
    return render(request, 'home/addRadio.html', context)
