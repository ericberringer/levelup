from django.db import models


class Event(models.Model):

    event_name = models.CharField(max_length=50)
    description = models.TextField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    date = models.DateTimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")