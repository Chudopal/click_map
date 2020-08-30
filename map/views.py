from django.shortcuts import render
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
            int(latlng["lat"]),
            int(latlng["lng"])
        )
        pointer = Pointer(point)
        pointer.save()
    if request.method == "GET":
        coords = Pointer.objects.all()
        context = {
            "coords":coords,
        }    
        return render(request, "map/log.html", context)