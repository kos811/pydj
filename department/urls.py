from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.department, name='department'),
    path('department/details/<int:id>', views.details, name='details'),
    path('department/testing', views.testing, name='testing'),
]