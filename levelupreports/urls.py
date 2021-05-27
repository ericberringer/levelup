from django.urls import path
from .views import usergame_list, eventuser_list

urlpatterns = [
    # first parameter is route, second is the method we are accessing in view
    path('reports/usergames', usergame_list),
    path('reports/userevents', eventuser_list),
]