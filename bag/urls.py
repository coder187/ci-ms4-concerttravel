from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<event_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<combination_key>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<combination_key>/', views.remove_from_bag, name='remove_from_bag')
]
