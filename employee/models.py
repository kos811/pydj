from django.db import models
from department.models import Department


# Create your models here.

class Employee(models.Model):
  id = models.BigIntegerField(primary_key=True)
  name = models.CharField(max_length=255)
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  department = models.ForeignKey(Department, on_delete=models.PROTECT)


  def __str__(self):
    return f"[{self.id}] | {self.name} | {self.salary} | {self.department}"