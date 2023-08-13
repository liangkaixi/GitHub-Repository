from django.urls import path
from . import views

urlpatterns = [
    path('class_allocation/', views.class_allocation, name='class_allocation'),
]