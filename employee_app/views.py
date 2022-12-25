from django.shortcuts import render
from django.http import HttpResponse

from . import views
from datetime import datetime
from .models import Employee, Role, Department

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    return render(request, 'all.html', context)

def add(request):
    depts = Department.objects.all()
    roles = Role.objects.all()
    context = {
        'depts' : depts,
        'roles': roles
    }

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = request.POST.get('dept', 1)
        role = request.POST.get('role', 2)
        print(dept)
        print(role)
        new_emp = Employee(first_name= first_name, last_name= last_name,salary=salary, bonus=bonus, phone= phone, dept_id = dept, role_id= role , hire_date = datetime.now() )
        new_emp.save()
        return HttpResponse("Employee added successfully")

    elif request.method == 'GET':
        return render(request, 'add.html', context)

    else:
        return HttpResponse("An error has occured")

def delete(request, emp_id=0):
    if emp_id:
        try:
            emp_to_delete= Employee.objects.get(id=emp_id)
            emp_to_delete.delete()
            return HttpResponse("EMp Removed")
        except:
            return HttpResponse("wrong id")
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    return render(request, 'delete.html') 

def filter(request):
    return render(request, 'filter.html')