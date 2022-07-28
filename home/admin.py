from django.contrib import admin
from .models import *

admin.site.register(Entite)
admin.site.register(Departement)
# admin.site.register(Ordonnance)
admin.site.register(DossierPatient)
admin.site.register(Radio)

