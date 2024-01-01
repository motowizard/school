from django.db import models

# Create your models here.
class Dept(models.Model):
    dname=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.dname

class Course(models.Model):
    cname=models.CharField(max_length=150,unique=True)
    department=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.cname

class Members(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(blank=True)
    dob=models.DateField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=250)
    purpose=models.CharField(max_length=50)

    def __str__(self):
        return self.name


