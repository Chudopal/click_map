from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('view', views.view_map, name="view"),
    path('log', views.click_log, name="log"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)