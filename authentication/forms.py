from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from PIL import Image
from django.forms import fields
from django.core.exceptions import ValidationError
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Adresse mail",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe",
                "class": "form-control"
            }
        ))

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patients
#         fields = ('docteur', 'prenom', 'nom', 'adresse', 'tel', 'dateNaissance', 'age', 'groupSanguin')
#         labels = {
#             'docteur': 'Docteur traitant',
#             'prenom': 'Prénom du patient',
#             'nom': 'Nom du patient',
#             'adresse': 'Adresse du patient',
#             'tel': 'Téléphone',
#             'dateNaissance': 'Date de naissance',
#             'age': 'Age',
#             'groupSanguin': 'Groupe sanguin',
#         }

#     def __init__(self, *args, **kwargs):
#         super(PatientFor/media/img_docteur/defaultDocteur.jpgm,self).__init__(*args, **kwargs)
#         self.fields['docteur'].empty_label = 'selection parmi les choix disponibles'
#         self.fields['groupSanguin'].empty_label = 'Choisir le groupe sanguin'
#         self.fields['prenom'].widget.attrs['placeholder'] = 'Prénom'
#         self.fields['nom'].widget.attrs['placeholder'] = 'Nom'
#         self.fields['adresse'].widget.attrs['placeholder'] = 'Adresse'
#         self.fields['tel'].widget.attrs['placeholder'] = 'Numéro de téléphone'
#         self.fields['dateNaissance'].widget.attrs['placeholder'] = 'Date de naissance'
#         self.fields['age'].widget.attrs['placeholder'] = 'Age'


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'prenom', 'nom', 'adresse', 'role', 'entite', 'tel')


class ProfileImageUpdateForm(forms.ModelForm):
    """Cette class permet de modifier seulement l'image de profile 
    de l'utilisateur connecté"""
    class Meta:
        model = Account
        fields = ('photo',)

class UserCreationForm2(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'prenom', 'nom', 'adresse', 'tel', 'role', 'entite')

class UpdateUserForm(forms.ModelForm):
    """Cette class permet de modifier les informations de l'utilisateur connecté"""
    class Meta:
        model = Account
        fields = ('email', 'prenom', 'nom', 'adresse', 'tel',)

class PasswordChangeFormEdit(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class' : 'form-control mb-2','placeholder':'Votre ancien mot de passe'})
        self.fields['new_password1'].widget.attrs.update({'class' : 'form-control mb-2','placeholder':'Votre nouveau mot de passe'})
        self.fields['new_password2'].widget.attrs.update({'class' : 'form-control mb-2','placeholder':'confirmer votre mot de passe '})
