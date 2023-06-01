from django.db import models

# Create your models here.
class Trademark(models.Model):
    categoryofwork = models.CharField(max_length=100)
    clientname = models.CharField(max_length=100)
    titleofwork = models.CharField(max_length=1000)
    modeofcontact = models.EmailField(max_length=100)
    referedby = models.CharField(max_length=1000)
    conntactnumber = models.IntegerField()
    emailid = models.EmailField(max_length=100)
    uid = models.CharField(max_length=20)
    date  = models.DateField()
    def __str__(self):
        return self.titleofwork

class Trademarkstatus(models.Model):
    uid = models.CharField(max_length=20)
    quotationstatus = models.CharField(max_length=20)
    quotedamount = models.CharField(max_length=20)
    toassignteam = models.CharField(max_length=20)
    projectduedate = models.CharField(max_length=20)
    trademarkcompleted = models.BooleanField(max_length=20)

    def __str__(self):
        return self.uid