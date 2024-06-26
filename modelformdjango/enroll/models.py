from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=70)
    student_password = models.CharField(max_length=70)
    

    # def __str__(self):
    #     return self.stuname
    