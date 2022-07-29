from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import * 

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ('nom', 'responsable')
        labels = {
            'nom': 'Nom du départemente',
            'responsable': 'Responsable du département',
        }

    def __init__(self, *args, **kwargs):
        super(DepartementForm,self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs['placeholder'] = 'Saisir le nom du département'
        self.fields['responsable'].widget.attrs['placeholder'] = 'Saisir le nom du responsable'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('docteur', 'prenom', 'nom', 'adresse', 'tel', 'age', 'sexe', 'proffesion', 'groupSanguin')
        labels = {
            'docteur': 'Docteur traitant',
            'prenom': 'Prénom du patient',
            'nom': 'Nom du patient',
            'adresse': 'Adresse du patient',
            'tel': 'Téléphone',
            'age': 'Age',
            'sexe': 'Sexe',
            'proffesion': 'Proffession',
            'groupSanguin': 'Groupe Sanguin',
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm,self).__init__(*args, **kwargs)
        # self.fields['docteur'].empty_label = 'Sélection parmi les choix disponibles'
        # self.fields['sexe'].empty_label = 'Sélection parmi les choix disponibles'
        # self.fields['proffesion'].empty_label = 'Sélection parmi les choix disponibles'
        # self.fields['groupSanguin'].empty_label = 'Sélection parmi les choix disponibles'
        self.fields['prenom'].widget.attrs['placeholder'] = 'Prénom'
        self.fields['nom'].widget.attrs['placeholder'] = 'Nom'
        self.fields['adresse'].widget.attrs['placeholder'] = 'Adresse'
        self.fields['tel'].widget.attrs['placeholder'] = 'Numéro de téléphone'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'
        self.fields['proffesion'].widget.attrs['placeholder'] = 'Proffession'


# class OrdonnanceForm(forms.ModelForm):
#     class Meta:
#         model = Ordonnance
#         fields = ('nom', 'medicaments', 'dosage', 'duree')
#         labels = {
#             'nom': 'Dénomination de l\'ordonnance',
#             'medicaments': 'Médicaments',
#             'dosage': 'Dosage',
#             'duree': 'Durée',
#         }

#     def __init__(self, *args, **kwargs):
#         super(OrdonnanceForm,self).__init__(*args, **kwargs)
#         self.fields['nom'].widget.attrs['placeholder'] = 'Saisir le nom de l\'ordonnance'
#         self.fields['medicaments'].widget.attrs['placeholder'] = ''
#         self.fields['dosage'].widget.attrs['placeholder'] = ''
#         self.fields['duree'].widget.attrs['placeholder'] = ''

class AjoutdossierForm(forms.ModelForm):
    class Meta:
        model = DossierPatient
        fields = ('docteur', 'diagnostic', 'traitement', 'paiement')
        labels = {
            'docteur': 'Praticien',
            'diagnostic': 'Diagnostique',
            'traitement': 'Traitement',
            'paiement': 'Paiement',
        }
    def __init__(self, *args, **kwargs):
        super(AjoutdossierForm,self).__init__(*args, **kwargs)
        self.fields['docteur'].empty_label = 'selection parmi les choix disponibles'
        self.fields['diagnostic'].required = True
        self.fields['traitement'].required = True
        self.fields['paiement'].required = True
#192.168.168.35 -> rapberry

class AntecedantForm(forms.ModelForm):
    class Meta:
        model = Antecedant
        fields = ('titre', 'antecedant')
        labels = {
            'titre': 'Titre',
            'antecedant': 'Antécedent',
        }
    def __init__(self, *args, **kwargs):
        super(AntecedantForm,self).__init__(*args, **kwargs)
        self.fields['titre'].empty_label = 'Nom de l\'antécedent'

        self.fields['titre'].required = True
        self.fields['antecedant'].required = True

class RadioForm(forms.ModelForm):
    class Meta:
        model = Radio
        fields = ('photo',)

class ChangePatientPhotoForm(forms.ModelForm):
    """Cette class sert uniquement à modifier l'image du profil d'un patient."""
    class Meta:
        model = Patients
        fields = ('docteur', 'prenom', 'nom', 'adresse', 'tel', 'age', 'sexe', 'proffesion', 'groupSanguin')