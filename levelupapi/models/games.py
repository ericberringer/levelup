from django.db import models
from django.db.models.deletion import CASCADE


class Games(models.Model):

        name = models.CharField(max_length=50)
        number_of_players = models.CharField(max_length=50)
        game_type_id = models.ForeignKey("Game_Type", on_delete=CASCADE)
        gamer_id = models.ForeignKey("Gamer", on_delete=CASCADE)