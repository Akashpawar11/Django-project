from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('all_memb/',views.all_memb, name='all_memb'),
    path('add_memb/',views.add_memb, name='add_memb'),
    path('remove_memb/',views.remove_memb, name='remove_memb'),
    path('remove_memb/<int:mem_id>', views.remove_memb, name='remove_memb'),
    path('filter_memb/',views.filter_memb, name='filter_memb'),
    path('facilities/',views.facilities, name='facilities'),
]
