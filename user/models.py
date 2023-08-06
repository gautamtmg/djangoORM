from django.db import models

# Create your models here.



class Person(models.Model):

    RED = "RD"
    BLUE = "BL"


    FAV_COLOUR = [
    # (1st for attribut value to store in database, 2nd for human readable from)
    (RED, 'Red'),
    (BLUE, 'Blue'),
]

    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50, choices=FAV_COLOUR)