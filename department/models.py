from django.db import models
# from employee.models import Employee

# Create your models here.

class Department(models.Model):
  id = models.BigIntegerField(primary_key=True)
  name = models.CharField(max_length=255)

  def __str__(self):
    return f"[{self.id}] {self.name}"