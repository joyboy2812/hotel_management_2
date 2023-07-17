from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelForm


# Create your views here.

def home(request):
    role = 'admin'
    context = {
        'role': role,
    }
    return render(request, 'hotels/home.html', context)


def manageHotel(request):
    hotels = Hotel.objects.all()
    role = 'admin'
    context = {
        'role': role,
        'hotels': hotels,
    }
    return render(request, 'hotels/manage_hotel.html', context)


def createHotel(request):
    form = HotelForm()
    role = 'admin'

    context = {
        'form': form,
        'role': role
    }

    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-hotel')

    return render(request, 'hotels/hotel_form.html', context)


def updateHotel(request, pk):
    hotel = Hotel.objects.get(id=pk)
    form = HotelForm(instance=hotel)
    role = 'admin'

    context = {
        'form': form,
        'role': role,
    }

    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('manage-hotel')

    return render(request, 'hotels/hotel_form.html', context)


def deleteHotel(request, pk):
    hotel = Hotel.objects.get(id=pk)
    role = 'admin'

    context = {
        'role': role,
        'hotel': hotel,
    }

    if request.method == 'POST':
        hotel.delete()
        return redirect('manage-hotel')

    return render(request, 'hotels/delete_template.html', context)
