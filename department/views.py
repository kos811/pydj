from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Department
from django.db.models import Subquery, OuterRef
from employee.models import Employee
from django.db.models.expressions import RawSQL

def department(request):
  departments = Department.objects.all().values()
  template = loader.get_template('all_departments.html')
  context = {
    'departments': departments,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  department = Department.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'department': department,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  name_map = {"id": "id", "name": "name", "employee_name":"employee_name", "max_salary":"max_salary"}
  raw = Department.objects.raw("""    
                             with sq  as (SELECT department_id, max(salary)  as max_salary
                                from employee_employee
                                group by department_id)
                              select id, name,  max_salary
                              from department_department d
                              join sq on sq.department_id = d.id                           
                               """,translations=name_map)

  template = loader.get_template('testing.html')
  

  context = {
    'raw':raw
  }
  return HttpResponse(template.render(context, request))