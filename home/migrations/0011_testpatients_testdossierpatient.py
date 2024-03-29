# Generated by Django 4.1.3 on 2022-12-20 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_alter_dossierpatient_paiement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, max_length=50, null=True)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('dateNaissance', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('sexe', models.CharField(blank=True, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10, null=True)),
                ('proffesion', models.CharField(blank=True, max_length=255, null=True)),
                ('docteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('entite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.entite')),
            ],
        ),
        migrations.CreateModel(
            name='TestDossierPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dateRV', models.DateField(blank=True, null=True)),
                ('diagnostic', models.TextField(blank=True, null=True)),
                ('traitement', models.TextField(blank=True, null=True)),
                ('remarques', models.TextField(blank=True, null=True)),
                ('paiement', models.CharField(blank=True, max_length=200, null=True)),
                ('docteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('entite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.entite')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.patients')),
            ],
        ),
    ]
