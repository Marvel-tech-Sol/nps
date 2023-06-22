from django.db import models

# Create your models here.

class Patentapplication(models.Model):
    uid = models.CharField(max_length=20)
    title = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=100)
    modeofcontact = models.CharField(max_length=50)
    referedby = models.CharField(max_length=100)
    conntactnumber = models.CharField(max_length=10)
    emailid = models.EmailField(max_length=50)
    patenttype = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    date = models.DateField()
    nda = models.CharField(max_length=30)
    idf = models.CharField(max_length=30)
    qua = models.CharField(max_length=30)

    def __str__(self):
        return self.uid


class PaymentStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)

    def __str__(self):
        return self.uid


class NDAStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=50)
    nda = models.CharField(max_length=50)

    def __str__(self):
        return self.uid


class NoveltyStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    duedate = models.DateField(null=True)
    rating = models.CharField(max_length=20)
    qc = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.uid


class DraftingStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    duedate = models.DateField(max_length=20, null=True)
    qc = models.CharField(max_length=20)
    drawings = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.uid


class DrawingStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    duedate = models.DateField(max_length=20,null=True)
    qc = models.CharField(max_length=20)
    drawings = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.uid


class DocumentationStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.uid


class FilingStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.uid


class ExaminationSatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    date = models.DateField(null=True)

    def __str__(self):
        return self.uid


class FerStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    duedate = models.DateField(max_length=20, null=True)
    qc = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.uid


class HearingStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    date = models.DateField(null=True)

    def __str__(self):
        return self.uid


class GrantsStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.uid

class IdeaDevelopmentStatus(models.Model):
    status = models.BooleanField(default=False)
    uid = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    duedate = models.DateField(max_length=20, null=True)
    qc = models.CharField(max_length=20)
    drawings = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.uid

class Assignedto(models.Model):
    uid = models.CharField(max_length=20)
    assignto = models.CharField(max_length=50)
    assignstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.uid
