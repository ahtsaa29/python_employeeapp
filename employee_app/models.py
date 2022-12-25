from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=50, null=False)
    dept_address = models.CharField(max_length=50)
    def __str__(self):
        return self.dept_name

class Role(models.Model):
    role_name = models.CharField(max_length=50, null=False)

    # for name to display
    def __str__(self):
        return self.role_name

class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField(default=0.0)
    bonus = models.FloatField(default=0.0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField()
    hire_date = models.DateField()
    def __str__(self):
        return "%s %s -- %s | %s"  %(self.first_name,self.last_name,self.dept,self.role)

    


