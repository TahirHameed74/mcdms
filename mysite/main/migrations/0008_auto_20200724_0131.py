# Generated by Django 3.0.2 on 2020-07-24 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200724_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carparameters',
            name='engineDetail',
            field=models.TextField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('LPG', 'LPG'), ('CNG', 'CNG'), ('Hybrid', 'Hybrid')]),
        ),
    ]
