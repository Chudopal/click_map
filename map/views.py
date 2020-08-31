from django.shortcuts import render
from .models import Pointer
from django.contrib.gis.geos import Point
import json


def view_map(request):
    """This function displays the map."""

    return render(request, "map/map.html")


def click_log(request):
    """This function accepts post and get requests for pointers. 
    It allows to display all pointers."""

    if request.method == "POST":
        latlng = json.loads(request.body)
        point = Point(
            float(latlng["lat"]),
            float(latlng["lng"]),
            srid=4326
        )
        print(dir(point))

        pointer = Pointer()
        
        print(dir(pointer.location))

        pointer.location = point
        print("HEREEEEEE")
        print(pointer)
        print("HEREEEEEE")
        pointer.save()
        return 302
    if request.method == "GET":
        coords = Pointer.objects.all()
        context = {
            "coords":coords,
        }    
        return render(request, "map/log.html", context)