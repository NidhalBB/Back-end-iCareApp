from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Sport(models.Model):
    SportId = models.AutoField(primary_key=True)
    SportName = models.CharField(max_length=500)
    Duree = models.IntegerField()

class User(AbstractUser):
    age = models.IntegerField(verbose_name='age')
    weight = models.IntegerField(verbose_name='weight')
    height = models.IntegerField(verbose_name='height')
    sport =  models.ManyToManyField(Sport, blank=True)