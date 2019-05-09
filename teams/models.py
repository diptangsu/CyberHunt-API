from django.db import models


class Team(models.Model):
    teamname = models.CharField(max_length=20, default='Team')
    password = models.CharField(max_length=20, default='password')

    name1 = models.CharField(max_length=50, default='John Doe')
    year1 = models.IntegerField(default=1)
    dept1 = models.CharField(max_length=10, default='CSE')
    phone1 = models.BigIntegerField(default=1234)

    name2 = models.CharField(max_length=50, default='Jane Doe')
    year2 = models.IntegerField(default=1)
    dept2 = models.CharField(max_length=10, default='CSE')
    phone2 = models.BigIntegerField(default=1234)

    def __str__(self):
        return self.teamname
