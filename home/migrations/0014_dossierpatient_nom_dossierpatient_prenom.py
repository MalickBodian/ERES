# Generated by Django 4.1.3 on 2022-12-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_testdossierpatient_nom_testdossierpatient_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossierpatient',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dossierpatient',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
