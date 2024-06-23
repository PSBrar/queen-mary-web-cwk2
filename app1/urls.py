from django.urls import path

#from . import views

from app1.views import car_view, one_car_view
from .api import cars_api, parts_api, del_car, del_part, all_parts_api, del_part_relation

'''
These are all the urls used within this app
'''

urlpatterns = [
    path("", car_view),
    path("api/cars", cars_api, name = "cars API"),
    path("api/parts/<int:car_id>/", parts_api, name = "parts API"),
    path('car/<int:car_id>/', one_car_view, name="one_car"),
    path("api/del_car/<int:car_id>/", del_car, name = "del_car API"),
    path("api/del_part/<int:part_id>/", del_part, name = "del_part API"),
    path("api/allparts", all_parts_api, name = "all parts API"),
    path("api/del_part/<int:car_id><int:part_id>/", del_part_relation, name = "del_part_relation API"),
]