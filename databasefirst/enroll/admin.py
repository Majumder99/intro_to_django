from django.contrib import admin
from enroll.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuname', 'stuemail')

# Register your models here.
admin.site.register(Student, StudentAdmin)

