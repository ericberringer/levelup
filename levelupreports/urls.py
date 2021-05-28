from django.urls import path
from .views import usergame_list, eventuser_list
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # first parameter is route, second is the method we are accessing in view
    path('reports/usergames', usergame_list),
    path('reports/userevents', eventuser_list),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)