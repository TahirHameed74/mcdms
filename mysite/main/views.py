from . import topsis
from django import forms
from django.contrib.auth.decorators import login_required
from django.template import loader
from django import template
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
import django.contrib.auth
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm


class HomeForm(forms.Form):
    post = forms.CharField()


# Create your views here.


def start(request):
    return render(request, 'main/start.html')


def about(request):
    return render(request, 'main/about.html')


def agents(request):
    return render(request, 'main/agents.html')


def apartment(request):
    return render(request, 'main/apartemnt.html')


def apartmentBuilding(request):
    return render(request, 'main/apartment-building.html')


def blogDetails(request):
    return render(request, 'main/blog-details.html')


def car(request):
    return render(request, 'main/car.html')


def columns(request):
    return render(request, 'main/columns.html')


def contact(request):
    return render(request, 'main/contact.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')


def faq(request):
    return render(request, 'main/faq.html')


def fullGallery(request):
    return render(request, 'main/full-gallery.html')


def gridListing(request):
    return render(request, 'main/gridlisting.html')


def index(request):
    return render(request, 'main/index.html')


def large_Map(request):
    return render(request, 'main/large-map.html')


def listing_Map(request):
    return render(request, 'main/listing-map.html')


def listing(request):
    return render(request, 'main/listing.html')


def property_search_result(request):
    # form = HomeForm(request.POST)
    # if form.is_valid():
    #     text = form.cleaned_data['post']
    #     print(text)
    print(request.POST.get('price'))
    # size(marla), price, city, town, old, floors, basement?, garden? room for servants, beds, bathrooms, park dist
    # mosque dist, school dist, market dist, hospital dist

    size = request.POST.get('size_sqft')
    price = request.POST.get('price')
    city = request.POST.get('city')
    if city == "All Cities":
        city = 1
    else:
        city = 1
    towns = request.POST.get('towns')
    if towns == "All Areas":
       towns = 1
    if towns == "Model Town":
       towns = 2
    elif towns == "Johar Town":
        towns = 3
    elif towns == "gulberg":
        towns = 4
    elif towns == "defence":
        towns = 5
    elif towns == "Faisal Town":
        towns = 6
    elif towns == "barkat market":
        towns = 7

    house_age = request.POST.get('house_age')
    floors = request.POST.get('floors')
    basement = request.POST.get('basement')
    if basement == 'With Basement':
        basement= 1
    else:
        basement = 0
    garden = request.POST.get('garden')
    if garden == 'With Garden':
        garden= 1
    else:
        garden = 0
    servants_room = request.POST.get('servants_room')
    bedroom = request.POST.get('bedroom')
    bathroom = request.POST.get('bathroom')
    park_dist =request.POST.get('park_dist')
    mosque_dist = request.POST.get('mosque_dist')
    school_dist = request.POST.get('school_dist')
    market_dist = request.POST.get('market_dist')
    hospital_dist = request.POST.get('hospital_dist')
    arr =[size,price,city,towns,house_age,floors,basement,garden,servants_room,bedroom,
               bathroom,park_dist,mosque_dist,school_dist, market_dist ,hospital_dist]
    print(arr)

    optimum_result = {'value': topsis.prop_recom(arr)}
    return render(request, 'main/property-search-result.html', context=optimum_result)


def car_search_result(request):
    brandType = request.POST.get('brandType')
    if brandType == "Toyota":
        brandType = 1
    elif brandType == "Honda":
        brandType = 2
    elif brandType == "BMW":
        brandType = 3
    elif brandType == "Suzuki":
        brandType = 4
    elif brandType == "Mercedes":
        brandType = 5
    elif brandType == "Audi":
        brandType = 6
    city = request.POST.get('city')
    if city == "All Cities":
        city = 1
    else:
        city = 1
    assemblyType = request.POST.get('assemblyType')
    if assemblyType == "Local":
        assemblyType = 1
    else:
        assemblyType = 0
    price = request.POST.get('price')
    engineCapacity = request.POST.get('engineCapacity')
    registrationCity = request.POST.get('registrationCity')
    if registrationCity == "Registration City":
        registrationCity = 1
    else:
        registrationCity = 1
    yearlyModel = request.POST.get('yearlyModel')

    if yearlyModel == "Yearly Model":
        yearlyModel = 1
    elif yearlyModel == "2020":
        yearlyModel = 1
    elif yearlyModel == "2019":
        yearlyModel = 2
    elif yearlyModel == "2018":
        yearlyModel = 3
    elif yearlyModel == "2017":
        yearlyModel = 4
    elif yearlyModel == "2016":
        yearlyModel = 5
    elif yearlyModel == "2015":
        yearlyModel = 6
    elif yearlyModel == "2014":
        yearlyModel = 7
    elif yearlyModel == "2013":
        yearlyModel = 8
    elif yearlyModel == "2012":
        yearlyModel = 9
    elif yearlyModel == "2011":
        yearlyModel = 10
    elif yearlyModel == "2010":
        yearlyModel = 11
    elif yearlyModel == "2009":
        yearlyModel = 12
    elif yearlyModel == "2008":
        yearlyModel = 13
    elif yearlyModel == "2007":
        yearlyModel = 14
    elif yearlyModel == "2006":
        yearlyModel = 15
    elif yearlyModel == "2005":
        yearlyModel = 16
    elif yearlyModel == "2004":
        yearlyModel = 17
    elif yearlyModel == "2003":
        yearlyModel = 18
    elif yearlyModel == "2002":
        yearlyModel = 19
    elif yearlyModel == "2001":
        yearlyModel = 20
    elif yearlyModel == "2000":
        yearlyModel = 21

    modelType = request.POST.get('modelType')
    if modelType =='Brand Model':
        modelType =1
    elif modelType == 'GLI':
        modelType = 1
    elif modelType == 'XLI':
        modelType = 2
    elif modelType == 'Mehran':
        modelType = 3
    elif modelType == 'Alto':
        modelType = 4

    engineChoice = request.POST.get('engineChoice')
    if engineChoice == 'Automatic or Manual':
        engineChoice = 1
    elif engineChoice == 'Manual':
        engineChoice = 1
    elif engineChoice == 'Automatic':
        engineChoice = 2

    color = request.POST.get('color')
    if color == "Color":
        color =1
    elif color == 'red':
        color = 1
    elif color == 'green':
        color = 2
    elif color == 'black':
        color = 3
    elif color == 'white':
        color = 4
    elif color == 'yellow':
        color = 5
    elif color == 'blue':
        color = 6
    elif color == 'pink':
        color = 7
    engineType = request.POST.get('engineType')
    if engineType == "Engine Details":
        engineType =1
    elif engineType == 'Diesel':
        engineType = 1
    elif engineType == 'Petrol':
        engineType = 2
    elif engineType == 'LPG':
        engineType = 3
    elif engineType == 'CNG':
        engineType = 4
    elif engineType == 'Hybrid':
        engineType = 5


    mileage = request.POST.get('mileage')
    if mileage == "Mileage":
        mileage =1
    elif mileage == '10000':
        mileage = 1
    elif mileage == '100000':
        mileage = 2
    elif mileage == '200000':
        mileage = 3
    elif mileage == '300000':
        mileage = 4
    elif mileage == '400000':
        mileage = 5

    arr =[brandType,city,assemblyType,price,engineCapacity,registrationCity,yearlyModel,modelType,engineChoice,color,engineType,mileage]
    print("arrrrrr")
    print(arr)
    optimum_result = {'value': topsis.car_recom(arr)}
    return render(request, 'main/car-search-result.html', context=optimum_result)


def listingMap(request):
    return render(request, 'main/listingmap.html')


def login(request):
    return render(request, 'main/login.html')


def miamiCity(request):
    return render(request, 'main/miami-city.html')


def news(request):
    return render(request, 'main/news.html')


def normalSlider(request):
    return render(request, 'main/normal-slider.html')


def office(request):
    return render(request, 'main/office.html')


def portfolio2(request):
    return render(request, 'main/portfolio-2.html')


def portfolio3(request):
    return render(request, 'main/portfolio-3.html')


def portfolio4(request):
    return render(request, 'main/portfolio-4.html')


def property(request):
    return render(request, 'main/property.html')


def rent(request):
    return render(request, 'main/rent.html')


def revSlider(request):
    return render(request, 'main/rev-slider.html')


def sale(request):
    return render(request, 'main/sale.html')


def shop(request):
    return render(request, 'main/shop.html')


def signup(request):
    return render(request, 'main/signup.html')


def singleFamily(request):
    return render(request, 'main/single-family.html')


def singleProperty(request):
    return render(request, 'main/single-property.html')


def submission(request):
    return render(request, 'main/submission.html')


def testimonials(request):
    return render(request, 'main/testimonials.html')


def typography(request):
    return render(request, 'main/typography.html')


def viall(request):
    return render(request, 'main/viall.html')


def admin_login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                django.contrib.auth.login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "main/admin-login.html", {"form": form, "msg": msg})


def admin_register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "main/admin-register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/admin-login/")
def admin_index(request):
    return render(request, "admin-index.html")


@login_required(login_url="/admin-login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
