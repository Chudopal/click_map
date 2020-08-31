from django.shortcuts import render
from .models import Pointer
from django.contrib.gis.geos import Point
import json
from django.views import generic


def view_map(request):
    """This function displays the map."""

    return render(request, "map/map.html")


class PointerListView(generic.ListView):
    """This class hanles POST and GET requests for pointers. 
    It allows to display all pointers."""
    
    model = Pointer
    paginate_by = 13
    template_name = "map/log.html"
    
    def post(self, request, *argv, **kwarg):
        """This is a handler for get queries"""

        latlng = json.loads(request.body)
        point = Point(
            float(latlng["lat"]),
            float(latlng["lng"]),
            srid=4326
        )

        pointer = Pointer(location=point)
        pointer.save()