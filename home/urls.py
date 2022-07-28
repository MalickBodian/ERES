from django.urls import path
from home import views

urlpatterns = [ 
    path("accueil", views.index, name='home'),
    ############################### Informations générales du patient ########################################
    path("details-patient/<int:id>/", views.DetailPatient, name='details'),
    ############################### CRUD de la table Patients ########################################
    path("patients", views.patient, name='patient'),
    path("ajout-patient", views.addPatient, name='addPatient'),
    # path("modif-patient/<int:id>/", views.editPatient, name='editPatient'),
    # path("delete-patient/<int:id>/", views.patientDelete, name='delPatient'),
    ############################### CRUD de la table DossierPatient ########################################
    path("dossier-patient/<int:id>/", views.dossier, name='dossier'),
    path("ajout-au-dossier/<int:id>/", views.addDossier, name='addDossier'),
    path("modification-dossier/<int:pk>/<int:id>/", views.editDossier, name='editDossier'),
    path("suppression-dossier/<int:pk>/<int:id>/", views.delDossier, name='delDossier'),
    ############################### CRUD de la table Radio ########################################
    path("radio-patient/<int:id>/", views.radioList, name='radio'),
    path("ajout-radio/<int:id>/", views.radioAdd, name='addRadio'),
    path("affichage-radio/<int:pk>/<int:id>/", views.viewRadio, name='viewRadio'),
]