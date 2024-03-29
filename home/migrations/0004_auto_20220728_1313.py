# Generated by Django 3.1.14 on 2022-07-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220728_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='groupSanguin',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sexe',
            field=models.CharField(blank=True, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10, null=True),
        ),
    ]
