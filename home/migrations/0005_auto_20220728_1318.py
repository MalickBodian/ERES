# Generated by Django 3.1.14 on 2022-07-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220728_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='dateNaissance',
            field=models.DateField(blank=True, null=True),
        ),
    ]
