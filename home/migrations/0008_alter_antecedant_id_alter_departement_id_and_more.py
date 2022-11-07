# Generated by Django 4.1.3 on 2022-11-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_dossierpatient_daterv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='departement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dossierpatient',
            name='dateRV',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dossierpatient',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='entite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='radio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
