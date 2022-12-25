from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('all',views.all,name="all"),
    path('add',views.add,name="add"),
    path('delete',views.delete,name="delete"),
    path('delete/<int:emp_id>',views.delete,name="delete"),
    path('filter',views.filter,name="filter"),

]