# Generated by Django 3.0.2 on 2020-07-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200609_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carparameters',
            name='assemblyType',
            field=models.TextField(choices=[('Imported', 'Imported'), ('Local', 'Local')], default='local'),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='brandType',
            field=models.TextField(choices=[('Toyota', 'Toyota'), ('Honda', 'Honda'), ('bmw', 'bmw'), ('Suzuki', 'Suzuki'), ('Mercedes', 'Mercedes'), ('Audi', 'Audi')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='city',
            field=models.TextField(choices=[('Lahore', 'Lahore')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='color',
            field=models.TextField(choices=[('red', 'red'), ('green', 'green'), ('black', 'black'), ('white', 'white'), ('yellow', 'yellow'), ('blue', 'blue'), ('pink', 'pink')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='engineType',
            field=models.TextField(choices=[('local', 'local'), ('imported', 'imported')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='registrationCity',
            field=models.TextField(choices=[('Lahore', 'Lahore')]),
        ),
        migrations.AlterField(
            model_name='carparameters',
            name='yearlyModel',
            field=models.TextField(choices=[('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000')]),
        ),
        migrations.AlterField(
            model_name='houseparameters',
            name='town',
            field=models.TextField(choices=[('Model Town', 'Model Town'), ('Johar Town', 'Johar Town'), ('gulberg', 'gulberg'), ('defence', 'defence'), ('Faisal Town', 'Faisal Town'), ('barkat market', 'barkat market')]),
        ),
    ]
