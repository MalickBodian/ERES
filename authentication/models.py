from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from home.models import Entite, Departement


class MyAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("L\'adresse email est obligatoire")
        
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)

def get_profile_image_filepath(self, filename):
    return f'img_docteur/docteur_{self.id}/{filename}'   

def get_default_profile_image():
    return 'img_docteur/defaultDocteur.jpg'

class Account(AbstractBaseUser):
    email             = models.EmailField(verbose_name='email', max_length=50, unique=True)
    created           = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    last_login        = models.DateTimeField(verbose_name='Date de la dérnière connexion', auto_now_add=True)
    is_admin          = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    is_staff          = models.BooleanField(default=True)
    is_superuser      = models.BooleanField(default=False)
    USER_TYPE_CHOICES = (("Responsable", "Responsable"), ("Agent", "Agent"))
    adresse           = models.CharField(max_length=255, null=True, blank=True)
    tel               = models.CharField(max_length=60, null=True, blank=True)
    role              = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, blank=True, null=True)
    prenom            = models.CharField(verbose_name='Prénom', max_length=30, blank=True, null=True)
    nom               = models.CharField(verbose_name='Nom', max_length=30, blank=True, null=True)
    entite            = models.ForeignKey(Entite, on_delete=models.SET_NULL, blank=True, null=True)
    departement       = models.ForeignKey(Departement, on_delete=models.SET_NULL, blank=True, null=True)
    photo             = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, blank=True, null=True, default=get_default_profile_image)

    USERNAME_FIELD = 'email'

    objects = MyAccountManager()

    def __str__(self):
        return '{} {}'.format(self.prenom, self.nom)

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{str(pk)}'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
