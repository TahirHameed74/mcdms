# Generated by Django 3.0.2 on 2020-07-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_houseparameters_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseparameters',
            name='city',
            field=models.TextField(choices=[('Lahore', 'Lahore')], default=1),
        ),
    ]