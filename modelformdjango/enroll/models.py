from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=70)
    student_password = models.CharField(max_length=70)

    def __str__(self):
        # This helps in debugging and whenever the model instance is printed
        return self.student_name
