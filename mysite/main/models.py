from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
town_choice = [('Model Town', 'Model Town'),
               ('Johar Town', 'Johar Town'),
               ('gulberg', 'gulberg'),
               ('defence', 'defence'),
               ('Faisal Town', 'Faisal Town'),
               ('barkat market', 'barkat market')]


city_choice = [('Lahore', 'Lahore')]

class houseParameters(models.Model):
    houseSize = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )
    price = models.BigIntegerField(
        default=0,
        validators=[MaxValueValidator(5000000000000), MinValueValidator(0)]
    )
    city = models.TextField(default=1,choices=city_choice)
    town = models.TextField(choices=town_choice)
    age = models.IntegerField()
    floor = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )
    isBasement = models.BooleanField()
    isGarden = models.BooleanField()
    servantRooms = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(2), MinValueValidator(0)]
    )
    numberOfBeds = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(20), MinValueValidator(1)]
    )
    bathroom = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(20), MinValueValidator(1)]
    )

    distanceFromPark = models.IntegerField(
        default=0,
    )
    distanceFromMosque = models.IntegerField(
        default=0,
    )
    distanceFromSchool = models.IntegerField(
        default=0,
    )
    distanceFromMarket = models.IntegerField(
        default=0,
    )
    distanceFromHospital = models.IntegerField(
        default=0,
    )


car_choice = [('Toyota', 'Toyota'),
              ('Honda','Honda'),
              ('bmw','bmw'),
              ('Suzuki', 'Suzuki'),
              ('Mercedes', 'Mercedes'),
              ('Audi', 'Audi')]

reg_choice = [('Lahore', 'Lahore')]
assembl_choice = [('Local', 'Local'),
                  ('Imported', 'Imported')]



eng_choice = [('Manual', 'Manual'),
              ('Automatic', 'Automatic')]

year_choice = [('2020', '2020'),
               ('2019', '2019'),
               ('2018', '2018'),
               ('2017', '2017'),
               ('2016', '2016'),
               ('2015', '2015'),
               ('2014', '2014'),
               ('2013', '2013'),
               ('2012', '2012'),
               ('2011', '2011'),
               ('2010', '2010'),
               ('2009', '2009'),
               ('2008', '2008'),
               ('2007', '2007'),
               ('2006', '2006'),
               ('2005', '2005'),
               ('2004', '2004'),
               ('2003', '2003'),
               ('2002', '2002'),
               ('2001', '2001'),
               ('2000', '2000')]

colors = [('red','red'),
    ('green','green'),
    ('black','black'),
    ('white','white'),
    ('yellow','yellow'),
    ('blue','blue'),
    ('pink','pink')]

brandModel = [('GLI','GLI'),
              ('XLI','XLI'),
              ('Mehran','Mehran'),
              ('Alto','Alto')]



engineDetailChoice = [('Diesel','Diesel'),
                      ('Petrol','Petrol'),
                      ('LPG','LPG'),
                      ('CNG','CNG'),
                      ('Hybrid','Hybrid')]


class carParameters(models.Model):
    brandType = models.TextField(choices=car_choice)
    city = models.TextField(choices=city_choice)
    assemblyType = models.TextField(
        default='local',
        choices=assembl_choice)
    price = models.IntegerField(
        default=0
    )
    engineCapacity = models.IntegerField()
    registrationCity = models.TextField(choices=reg_choice)
    yearlyModel = models.TextField(choices=year_choice)
    brandModel = models.TextField(choices=brandModel)
    engineType = models.TextField(choices=eng_choice)
    color = models.TextField(choices=colors)
    engineDetail = models.TextField(choices=engineDetailChoice)
    Mileage = models.BigIntegerField(
        default=0
    )
