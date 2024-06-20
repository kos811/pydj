from django.contrib import admin
from .models import Department

# Register your models here.
# admin.site.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
  list_display = ("id", "name")

admin.site.register(Department, DepartmentAdmin)