from django.db import models

# Create your models here.
class teachers(models.Model):
    tname=models.CharField(max_length=20)
    texperience=models.IntegerField()
    texperties=models.CharField(max_length=20)
    tcontact=models.IntegerField()
    
    def __str__(self):
        return self.tname

class students(models.Model):
    Sname=models.CharField(max_length=20)
    Sage=models.IntegerField()
    Scontact=models.IntegerField()
    
    def __str__(self):
        return self.Sname
    
class joinclass(models.Model):
    teachers=models.ForeignKey(teachers,on_delete=models.CASCADE)
    students=models.ForeignKey(students,on_delete=models.CASCADE)
    courses=models.CharField(max_length=20)
    date=models.DateField()
    slot=models.TimeField()
