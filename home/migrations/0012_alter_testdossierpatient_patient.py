# Generated by Django 4.1.3 on 2022-12-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_testpatients_testdossierpatient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdossierpatient',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.testpatients'),
        ),
    ]