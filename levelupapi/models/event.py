from django.db import models


class Event(models.Model):

    event_name = models.CharField(max_length=50)
    description = models.TextField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    date = models.DateTimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="events")
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
    time = models.TimeField()

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    @property
    def attendees_count(self):
        return self.__attendees_count

    @attendees_count.setter
    def attendees_count(self, value):
        self.__attendees_count = value