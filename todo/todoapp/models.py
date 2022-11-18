from django.db import models
from todoapp.manager import CustomManager

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=500)
    date=models.DateField()
    is_deleted=models.CharField(max_length=10)
    '''
    def __str__(self):
        return self.title
        #return self.details
        #return self.date
    '''




#Course Model
class Course(models.Model):
    cname=models.CharField(max_length=50)
    cdur=models.IntegerField()
    ccat=models.CharField(max_length=50)
    cprice=models.IntegerField()


    #cobj=models.Manager()
    ccustomobj=CustomManager()