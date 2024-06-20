from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Department
from django.db.models import Avg, F, Window, Max, Subquery, OuterRef
from employee.models import Employee

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
  departments = Department.objects.all()
  newest=Employee.objects.filter(department=OuterRef('pk')).order_by('-salary')
  q = Department.objects.annotate(
    max_salary=Subquery(newest.values('salary')[:1])).order_by('max_salary') 
  template = loader.get_template('testing.html')
  context = {
    'department': departments,
    'q':q
    # 'employees': employees,
  }
  return HttpResponse(template.render(context, request))