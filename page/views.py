from django.shortcuts import render
from .models import Vehicle


def main_page(request):
    context = {}
    vehicles = Vehicle.objects.all()
    car = Vehicle.objects.filter(size="car").all()
    van = Vehicle.objects.filter(size="van").all()
    bike = Vehicle.objects.filter(size="bike").all()
    truck = Vehicle.objects.filter(size="truck").all()
    bus = Vehicle.objects.filter(size="bus").all()

    context['total'] = len(vehicles)
    context['car'] = len(car)
    context['van'] = len(van)
    context['bike'] = len(bike)
    context['truck'] = len(truck)
    context['bus'] = len(bus)

    return render(request, 'page/main/cards.html', context)


# def vehicle_cout(request):

#     return render(request, 'page/main/vehicle_count.html', context)
