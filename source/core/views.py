from django.shortcuts import render
from django.http import HttpResponse

from .models import District, Apartment


def index(request):

    arguments = ["room_count", "price", "area_total", "bood_comp", "district"]

    if request.GET:
        values = [ (request.GET[arg] if request.GET[arg] else None)  for arg in arguments]
    else:
        values = [ None for arg in arguments]


    (room_count, 
    price, 
    area_total, 
    bood_comp, 
    district) = values

    apartments = Apartment.objects.all()
    if room_count:
        apartments = Apartment.objects.filter(room_count__exact=int(room_count))
    if price:
        apartments = apartments.filter(price__level__lte=int(price))
    if area_total:
        apartments = apartments.filter(area_total__gte=int(area_total))
    if bood_comp:
        apartments = apartments.filter(project__bood_company__name__iregex=r'{}'.format(bood_comp))
    if district:
        apartments = apartments.filter(project__district__name__iregex=r'{}'.format(district))

    context = {"apartments_list": apartments,
               "current_room_count": room_count,
               "current_price": price,
               "current_area_total": area_total,
               "current_bood_comp": bood_comp,
               "current_district": district
            }
    return render(request, 'core/index.html', context)
    


