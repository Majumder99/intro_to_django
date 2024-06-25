from django.db import models

# Create your models here.
class Student(models.Model):
    studid=models.IntegerField()
    stuname=models.CharField(max_length=30)
    stuemail=models.EmailField()
    stupass=models.CharField(max_length=30)
    common=models.CharField(max_length=30, default='common')
    

    def __str__(self):
        return self.stuname
    