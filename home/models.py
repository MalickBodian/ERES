from django.db import models
import authentication.models

def get_profile_image_filepath(self, filename):
    return f'img_patient/patient_{self.id}/{filename}'   

def get_default_profile_image():
    return 'img_patient/defaultPatient.jpg'

def get_radio_image_filepath(self, filename):
    return f'Radios/patient_{self.id}/{filename}'

# def get_patient_image_filepath(self, filename):
#     return f'img_patient/patient_{self.id}/{filename}'

# def get_default_patient_image():
#     return 'img_patient/defaultPatient.jpg'

class Entite(models.Model):
    TYPE_CHOICES = [
        ('Hopital', 'Hopital'),
        ('Clinique', 'Clinique'),
        ('Pharmacie', 'Pharmacie'),
    ]
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    type = models.CharField(max_length=50, default='Clinique', choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Patients(models.Model):
    BLOOD_TYPE_CHOICES = (("O+", "O+"), ("O-", "O-"), ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"))
    GENDER_CHOICES = (("Masculin", "Masculin"), ("Feminin", "Feminin"))
    docteur = models.ForeignKey("authentication.Account", on_delete=models.SET_NULL, blank=True, null=True)
    entite = models.ForeignKey(Entite, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    dateNaissance = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    sexe = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    proffesion = models.CharField(max_length=255, blank=True, null=True)
    groupSanguin = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    photo = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, blank=True, null=True, default=get_default_profile_image)

    def __str__(self):
        return '{} {}'.format(self.prenom, self.nom)

    def get_patient_image_filename(self):
        return str(self.patient_image)[str(self.patient_image).index(f'patient_images/{str(pk)}'):]



class Departement(models.Model):
    nom = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    entite = models.ForeignKey(Entite, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Radio(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True)
    docteur = models.ForeignKey("authentication.Account", on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ImageField(max_length=255, upload_to=get_radio_image_filepath, blank=True, null=True)

#class Rdv

# class Ordonnance(models.Model):
#     entite = models.ForeignKey(Entite, on_delete=models.CASCADE)
#     nom = models.CharField(max_length=50)
#     created = models.DateTimeField(auto_now=False, auto_now_add=False)
#     patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True)
#     docteur = models.ForeignKey("authentication.Docteur", on_delete=models.SET_NULL, blank=True, null=True)
#     medicaments = models.TextField(blank=True, null=True)
#     dosage = models.TextField(blank=True, null=True)
#     duree = models.TextField(blank=True, null=True)

#     def __str__(self):
#             return self.nom


class DossierPatient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dateRV = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    entite = models.ForeignKey(Entite, on_delete=models.CASCADE)
    docteur = models.ForeignKey("authentication.Account", on_delete=models.SET_NULL, blank=True, null=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    traitement = models.TextField(blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    paiement = models.CharField(max_length=200, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)

class Antecedant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length=20, blank=True, null=True)
    antecedant = models.TextField(blank=True, null=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True)
    




class TestPatients(models.Model):
    BLOOD_TYPE_CHOICES = (("O+", "O+"), ("O-", "O-"), ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"))
    GENDER_CHOICES = (("Masculin", "Masculin"), ("Feminin", "Feminin"))
    docteur = models.ForeignKey("authentication.Account", on_delete=models.SET_NULL, blank=True, null=True)
    entite = models.ForeignKey(Entite, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    dateNaissance = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    sexe = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    proffesion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.prenom, self.nom)


class TestDossierPatient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dateRV = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    entite = models.ForeignKey(Entite, on_delete=models.CASCADE)
    docteur = models.ForeignKey("authentication.Account", on_delete=models.SET_NULL, blank=True, null=True)
    patient = models.ForeignKey(TestPatients, on_delete=models.CASCADE, blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    traitement = models.TextField(blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    paiement = models.CharField(max_length=200, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)

    