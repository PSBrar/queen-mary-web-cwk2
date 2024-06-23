from django.http import JsonResponse
from .models import VW_Car, Part
from django.shortcuts import get_object_or_404

def cars_api(request):
    ''' 
    entry point for doing GET request for cars list 
    '''
    return JsonResponse({
        'cars': [
            VW_Car.to_dict()
            for VW_Car in VW_Car.objects.all()
        ]
    })

def parts_api(request, car_id):
    ''' 
    entry point for doing GET request for parts list
    '''
    return JsonResponse({
        'parts': [
            Part.to_dict()
            for Part in ((VW_Car.objects.get(pk=car_id)).parts.all())
        ]
    })

def all_parts_api(request):
    ''' 
    entry point for doing GET request for cars list
    '''
    return JsonResponse({
        'parts': [
            Part.to_dict()
            for Part in Part.objects.all()
        ]
    })

def del_car(request,car_id):
    ''' 
    entry point for doing DELETE requests for cars list 
    '''
    if request.method == "DELETE":
        car = get_object_or_404(VW_Car, id=car_id)
        car.delete()
        return JsonResponse({})
    else:
        return HttpResponseBadResponse("Invalid method")

def del_part(request,part_id):
    ''' 
    entry point for doing DELETE requests for parts list 
    '''
    if request.method == "DELETE":
        part = get_object_or_404(Part, id=part_id)
        part.delete()
        return JsonResponse({})
    else:
        return HttpResponseBadResponse("Invalid method")

def del_part_relation(request,car_id,part_id):
    ''' 
    entry point for doing DELETE requests for just the car and parts relations 
    '''
    
    if request.method == "DELETE":
        part = get_object_or_404(VW_Car.car_parts, id=part_id)
        part.delete()
        return JsonResponse({})
    else:
        return HttpResponseBadResponse("Invalid method")