from django.db import models


# Create your models here.
class Copyright(models.Model):
    Categoryofwork = models.CharField(max_length=100)
    clientname = models.CharField(max_length=100)
    titleofwork = models.CharField(max_length=1000)
    modeofcontact = models.CharField(max_length=100)
    referedby = models.CharField(max_length=1000)
    conntactnumber = models.IntegerField()
    emailid = models.EmailField(max_length=100)
    uid = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    date  = models.DateField()

    def __str__(self):
      return self.uid


class Copyrightstatus(models.Model):
    uid = models.CharField(max_length=20)
    quotationstatus = models.CharField(max_length=20)
    quotedamount = models.CharField(max_length=20)
    toassignteam = models.CharField(max_length=20)
    projectduedate = models.CharField(max_length=20)
    copyrightcompleted = models.BooleanField(max_length=20)


    def __str__(self):
        return self.uid