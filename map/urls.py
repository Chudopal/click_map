from django.urls import path
from . import views

urlpatterns = [
    path('view', views.view_map, name="view"),
    path('log', views.click_log, name="log"),
]