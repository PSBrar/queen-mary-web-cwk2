from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Part, VW_Car
from django.urls import reverse

def index(request):
    return HttpResponse("app1 working")

def car_view(request):
    '''
    This view is used for the cars.html page and simply passes in the cars objects from the VW_Car model table
    '''
    cars = VW_Car.objects.all()
    return render(request, "cars.html", {
        "cars": cars
    })
    #HttpResponse("hello world")

def one_car_view(request, car_id):
    '''
    This view is used for the part.html page . It takes in a car PK, searches for the parts associated with that
    VW_Car record and returns a dictionary containing an API url for later, the car PK and the car name
    '''
    single_car = VW_Car.objects.get(pk=car_id)
    car_parts = single_car.parts.all()
    return render(request, "part.html", {
        "car_id": car_id,
        "car_name": single_car,
        "api": reverse("parts API", kwargs={"car_id": car_id})
    })

#def put_form(request):
#    return render(request, updateform.html{
#
#    })