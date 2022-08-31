from django.db import models


# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_age = models.IntegerField()
    staff_salary = models.FloatField(default=1.0)


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()


class Animal(models.Model):
    animal_name = models.CharField(max_length=100)
    animal_leg = models.IntegerField()
