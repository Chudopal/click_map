from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def view_map(request):
    return render(request, "map/map.html")


def click_log(request):
    pass