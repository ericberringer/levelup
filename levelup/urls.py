from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from levelupapi.views import register_user, login_user
from levelupapi.views import GameTypeView, GameView, EventView, Profile


# Default Router will allow a client to submit either one of the url's in the router.register
# i.e. /gametypes for all gametypes, and /gametype/1 for a single game type by id
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
router.register(r'profile', Profile, 'profile')


urlpatterns = [
    path('admin/', admin.site.urls),
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    # This gives us access to the url paths in our levelupreports application
    path('', include('levelupreports.urls')),
]