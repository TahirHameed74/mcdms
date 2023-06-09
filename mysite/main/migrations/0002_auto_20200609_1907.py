# Generated by Django 3.0.5 on 2020-06-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carparameters',
            name='assemblyType',
            field=models.TextField(choices=[('Japanese', 'Japanese'), ('Local', 'Local')], default='local'),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='brandType',
            field=models.TextField(choices=[('Toyota', 'Toyota'), ('Suzuki', 'Suzuki'), ('Hyundai', 'Hyundai')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='city',
            field=models.TextField(choices=[('Lahore', 'Lahore'), ('Karachi', 'Karachi')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='engineType',
            field=models.TextField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='registrationCity',
            field=models.TextField(choices=[('Lahore', 'Lahore'), ('Karachi', 'Karachi')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='yearlyModel',
            field=models.TextField(choices=[('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013')]),
        ),
        migrations.AlterField(
            model_name='houseparameters',
            name='town',
            field=models.TextField(choices=[('Johar Town', 'Johar Town'), ('Faisal Town', 'Faisal Town'), ('Model Town', 'Model Town'), ('Garden Town', 'Garden Town'), ('Wapda Town', 'Wapda Town'), ('Township', 'Township')]),
        ),
    ]
