from django.db import models

class Team(models.Model):
    teamname = models.CharField(max_length=20)

    def __str__(self):
        return self.teamname
