# Generated by Django 4.1.3 on 2022-11-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_antecedant_id_alter_departement_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossierpatient',
            name='remarques',
            field=models.TextField(blank=True, null=True),
        ),
    ]