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
  newest=Employee.objects.filter(department=OuterRef('pk')).order_by('-salary')
  querySet = Department.objects.annotate(
    max_salary=Subquery(newest.values('salary')[:1])).order_by('-max_salary') 
  
  name_map = {"id": "id", "name": "name", "employee_name":"employee_name", "max_salary":"max_salary"}
  raw = Department.objects.raw("""                               
                                with cte as (
                                  select
                                    id,
                                    department_id,
                                    salary,
                                    name,
                                    dense_rank() over (partition by department_id order by salary desc)  as rank
                                  from employee_employee )
                                select
                                  d.id,
                                  d.name,
                                  cte.name as employee_name,
                                  cte.salary as max_salary
                                from department_department d
                                join cte on cte.department_id = d.id
                                where rank = 1
                                order by cte.salary desc
                               """,translations=name_map)

  template = loader.get_template('testing.html')
  

  context = {
    'querySet':querySet,
    'raw':raw
    # 'employees': employees,
  }
  return HttpResponse(template.render(context, request))