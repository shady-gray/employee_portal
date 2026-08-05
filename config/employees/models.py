from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    hire_date = models.DateField()

    def __str__(self):
        return self.full_name
