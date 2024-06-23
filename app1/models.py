from django.db import models
from django.urls import reverse

# My relationship is a many to many relationship between cars and parts 

# Each model must also have at least two fields 
#(other than the id field and the many-to-many field), 
#and these must include CharField, IntegerField and DateField

class VW_Car(models.Model):
    '''
    This is the main model for the car table
    '''
    car_name = models.CharField(max_length=20)
    parts = models.ManyToManyField(
        'Part',
        blank=True,
        symmetrical=False,
        related_name='car_parts'
    )
    car_colour = models.CharField(max_length=20)
    car_number_of_doors = models.IntegerField(default=0)
    car_manufacture_date = models.DateField("date car was manufactured")
    car_transmission = models.CharField(max_length=20)
    car_price = models.IntegerField(default=0)

    def __str__(self):
        '''
        Returns a string of the name for each VW_Car record        
        '''
        return self.car_name

    def to_dict(self):
        '''
        Converts the model's data into a dictionary for each record specified by the calling function.
        '''
        return ({
            "id":self.id,
            "car_name": self.car_name,
            "car_colour": self.car_colour,
            "car_number_of_doors": self.car_number_of_doors,
            "car_manufacture_date": self.car_manufacture_date,
            "car_transmission": self.car_transmission,
            "car_price": self.car_price,
            "url": reverse("one_car", kwargs={"car_id": self.id}),
            "api": reverse("del_car API", kwargs={"car_id": self.id}),
            "editBoolean": False
            
        })

class Part(models.Model):
    '''
    This is the main model for the part table
    '''
    part_name = models.CharField(max_length=20)
    part_number = models.IntegerField(default=0)
    part_type = models.CharField(max_length=50)
    part_manufacture_date = models.DateField("date part was manufactured")

    def __str__(self):
        '''
        Returns a string of the name for each Part record        
        '''
        return self.part_name

    def to_dict(self):
        '''
        Returns a dictionary containing model data
        '''
        return ({
            "id":self.id,
            "name": self.part_name,
            "num": self.part_number,
            "type": self.part_type,
            "manufacture_date": self.part_manufacture_date,
            "api": reverse("del_part API", kwargs={"part_id": self.id})
        })
