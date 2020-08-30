from django.shortcuts import render
from django.shortcuts import render
import json


def view_map(request):
    """This function displays the map."""

    return render(request, "map/map.html")


def click_log(request):
    """This function accepts post and get requests for pointers. 
    It allows to display all pointers."""

    if request.method == "POST":
        print("HEREEEEEEE1")
        latlng = json.loads(request.body)
        print(latlng["lat"])
        print(latlng["lng"])
    if request.method == "GET":
        print("HEREEEEEEE2")    
    