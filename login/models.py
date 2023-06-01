from django.db import models


# Create your models here.

class Usermodel(models.Model):
    username = models.CharField(max_length=30)
    teamname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class TeamModels(models.Model):
    team = models.CharField(max_length=30)

    def __str__(self):
        return self.team

class referdby(models.Model):
    names = models.CharField(max_length=100)

    def __str__(self):
        return self.names