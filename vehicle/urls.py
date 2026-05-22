from django.urls import path
from . import views 

urlpatterns = [
    path('', views.add_vehicle, name='add_vehicle'),
    path('vehicle_reg_form/', views.add_vehicle, name='vehicle_reg_form'),
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
    path('vehicle_list/edit/<int:pk>/', views.edit_vehicle, name="edit_vehicle")
]