from django.shortcuts import render, redirect,get_object_or_404
from .forms import VehicleForm
from .models import Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  
    else:
        form = VehicleForm()
    context = {
        "form": form
    }
    return render(request, 'vehicle/vehicle_reg_form.html', context)

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {
        "vehicles": vehicles
    }
    return render(request, 'vehicle/vehicle_list.html', context)

@login_required
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  
    else:
        form = VehicleForm(instance=vehicle)
    context = {
        "form": form
    }
    return render(request, 'vehicle/vehicle_reg_form.html', context)
