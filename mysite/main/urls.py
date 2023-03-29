"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.urls import path, include
app_name = "main"

urlpatterns = [
    path("", views.start,name='main'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('apartemnt/', views.apartment, name='apartment'),
    path('apartment-building/', views.apartmentBuilding, name='apartmentbuilding'),
    path('blog-details/', views.blogDetails, name='blogdetails'),
    path('car/', views.car, name='car'),
    path('columns/', views.columns, name='columns'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('faq/', views.faq, name='faq'),
    path('full-gallery/', views.fullGallery, name='fullgallery'),
    path('gridlisting/', views.gridListing, name='gridlisting'),
    path('index/', views.index, name='index'),
    path('large-map/', views.large_Map, name='largemap'),
    path('listing-map/', views.listing_Map, name='listingmap'),
    path('listing/', views.listing, name='listing'),
    path('property-search-result/', views.property_search_result, name='property-search-result'),
    path('car-search-result/', views.car_search_result, name='car-search-result'),
    path('listingmap/', views.listingMap, name='listingmap2'),
    path('login/', views.login, name='login'),
    path('miami-city/', views.miamiCity, name='miamicity'),
    path('news/', views.news, name='news'),
    path('normal-slider/', views.normalSlider, name='normalslider'),
    path('office/', views.office, name='office'),
    path('portfolio-2/', views.portfolio2, name='portfolio2'),
    path('portfolio-3/', views.portfolio3, name='portfolio3'),
    path('portfolio-4/', views.portfolio4, name='portfolio4'),
    path('property/', views.property, name='property'),
    path('rent/', views.rent, name='rent'),
    path('rev-slider/', views.revSlider, name='revslider'),
    path('sale/', views.sale, name='sale'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('single-family/', views.singleFamily, name='singlefamily'),
    path('single-property/', views.singleProperty, name='singleproperty'),
    path('start/', views.start, name='start'),
    path('submission/', views.submission, name='submission'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('typography/', views.typography, name='typography'),
    path('viall/', views.viall, name='viall')

]
