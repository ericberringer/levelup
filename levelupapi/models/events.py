from django.db import models
from django.db.models.deletion import CASCADE


class Events(models.Model):

    event_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    game_id = models.ForeignKey("Games", on_delete=CASCADE)