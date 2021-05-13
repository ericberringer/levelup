from django.contrib.auth.models import User
from levelupapi.models import gamer
from django.db import models


class Game(models.Model):

        gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
        game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
        maker = models.CharField(max_length=50)
        title = models.CharField(max_length=50)
        number_of_players = models.IntegerField()
        skill_level = models.IntegerField()

        @property
        def event_count(self):
                return self.__event_count

        @event_count.setter
        def event_count(self, value):
                self.__event_count = value