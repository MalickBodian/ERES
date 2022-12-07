# from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import redirect
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse



@login_required(login_url="/")
def index(request):
    patients = Patients.objects.filter(entite = request.user.entite).count()
    doctors = Account.objects.filter(entite = request.user.entite).count()
    context = {'patient':patients, 'doctor':doctors}
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
    submitted = False
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.instance.entite = request.user.entite
            form.save()
            return HttpResponseRedirect('/home/patients')
    else:
        form = PatientForm
        if 'submitted' in request.GET:
            submitted = True
    form = PatientForm
    return render(request, 'home/ajoutPatient.html', {'form':form, 'submitted':submitted})

@login_required(login_url="/")
def editPatient(request, id=0):
    # obj = get_object_or_404(Patients, id=id)
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            traitement = Patients.objects.get(pk=id)
            form = PatientForm(instance=traitement) 
        return render(request, "home/modifPatient.html", {'form':form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            traitement = Patients.objects.get(pk=id)
            form = PatientForm(request.POST, instance = traitement)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home/patients')

def patientDelete(request, id):
    patient = Patients.objects.get(pk=id)
    patient.delete()
    return HttpResponseRedirect('/home/patients')


############################### Informations générales du patient ########################################
@login_required(login_url="/")
def DetailPatient(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    antecedents = Antecedant.objects.filter(patient = obj).order_by('-id')
    forms = ChangePatientPhotoForm(request.POST or None, instance = obj)
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
        'form':form,
        'forms':forms
    }
    return render(request, 'home/detail-patient.html', context)

@login_required(login_url="/")
def changePhoto(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    forms = ChangePatientPhotoForm(request.POST or None, instance = obj)
    context= {'forms': forms}
    if forms.is_valid():
        forms.instance.photo = request.FILES['image']
        forms.save()
        return redirect('details', id)
    else:
        context = {'forms': forms}
    return render(request, 'home/detail-patient.html', context)
    # context = {'obj':obj}
    # if request.method == 'POST':
    #     radio = Patients()
    #     # radio.patient = obj
    #     radio.photo = request.FILES['image']
    #     radio.save()
    #     return redirect('details', id)
    # else:
    #     context = {'obj':obj}
    # return render(request, 'home/addRadio.html', context)

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
        'dossierPatient':DossierPatient.objects.filter(patient = obj).order_by("-created")
    }
    return render(request, 'home/dossierPatient.html', context)

@login_required(login_url="/")
def addDossier(request, id=0):
    obj = get_object_or_404(Patients, id=id)
    submitted = False
    if request.method == 'POST':
        form = AjoutdossierForm(request.POST)
        if request.POST.get('date'):
            if form.is_valid():
                form.instance.dateRV = request.POST.get('date')
                form.instance.patient = obj
                form.instance.entite = request.user.entite
                form.save()
                return redirect('dossier', id)
        else:
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
    context= {'form': form, 'ajout':patient}
    if request.POST.get('date'):
        if form.is_valid():
            form.instance.dateRV = request.POST.get('date')
            form.save()
            return redirect('dossier', pk)
    if not request.POST.get('date'):
        if form.is_valid():
            form.save()
            return redirect('dossier', pk)
    else:
        context = {'form': form, 'ajout':patient, 'doss':obj}
    return render(request, 'home/editDossier.html', context)

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


@csrf_exempt
def diag(request):
    libelle = 'yes'
    if request.method =='POST':
        f = open('home/diagnosis.json',)
        datas = json.load(f)
        for data in datas:
            DossierPatient.objects.get_or_create(pk=data['pk'], 
            patient=Patients.objects.get(id = data['patient']),
            diagnostic=data['diagnostic'],
            traitement=data['traitement'],
            remarques=data['remarks'],
            paiement=data['bill'],
            entite=Entite.objects.get(nom = 'clinic dentaire'))
    return HttpResponse(json.dumps({'libelle': libelle}))


@login_required(login_url="/")
def get_patients(request):
    f = open('home/patients.json',)
    datas = json.load(f)
    for data in datas:
        Patients.objects.get_or_create(pk=data['pk'], 
        prenom=data['prenom'],
        nom=data['nom'],
        adresse=data['adresse'],
        tel=data['tel'],
        sexe=data['genre'],
        proffesion=data['proffession'],
        entite=request.user.entite)
    return redirect('home')
@login_required(login_url="/")
def get_diagnosis(request):
    f = open('home/diagnosis.json',)
    datas = json.load(f)
    for data in datas:
        DossierPatient.objects.get_or_create(pk=data['pk'], 
        patient=Patients.objects.get(id = data['patient']),
        diagnostic=data['diagnostic'],
        traitement=data['traitement'],
        remarques=data['remarks'],
        paiement=data['bill'],
        entite=request.user.entite)
    return redirect('home')