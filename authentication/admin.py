from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserCreationForm, UserChangeForm

admin.site.register(Account)

