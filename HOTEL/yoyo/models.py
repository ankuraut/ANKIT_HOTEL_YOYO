from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_TYPES={
        ('NOR','NORMAL'),
        ('ACC','AC'),
        ('NAC','NON-AC'),
        ('KIG','KING'),
        ('QUE','QUEEN'),
        ('XYX','COUPLE-FRIENDLY'),
    }
    MEAL_TYPES={
        ('BKFST','BREAKFAST'),
        ('LUC','LUNCH'),
        ('DIN','DINNER'),
        ('NA','NOTHING'),
    }
    IDPROOF_TYPES={
        ('AAD','AADHAR'),
        ('DLI','DRIVING-LICENCE'),
        ('PAS','PASSPORT'),
    }
    number = models.IntegerField()
    types = models.CharField(max_length=3, choices=ROOM_TYPES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    meals = models.CharField(default="none",max_length=5, choices=MEAL_TYPES)
    idcard = models.CharField(default="none",max_length=3, choices=IDPROOF_TYPES)

    def __str__(self):
        return f'{self.number} with {self.types} & {self.beds} bed , {self.capacity} person need {self.meals}'    # F is a new format to represent the string
    