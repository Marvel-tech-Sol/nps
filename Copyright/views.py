import random

from django.apps import apps
from django.shortcuts import render, redirect
from .models import Copyright


# Create your views here
def random_string(ReferedBy):
    unique_id = ReferedBy[0:2] + "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    return unique_id


def Copyrighttableview(r):
    c = Copyright.objects.all()
    ass = apps.get_model('Patent', 'Assignedto').objects.all()
    return render(r, "copyright/Copyrighttable.html", {'c': c, 'a': ass})


def Copyrightstatusview(r, uid):
    return render(r, "copyright/Copyrightstatus.html")


def Copyrightapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    users = apps.get_model('login', 'Usermodel').objects.all()
    if request.method == 'POST':
        categoryofwork = request.POST['categoryofwork']
        clientname = request.POST['clientname']
        titleofwork = request.POST['titleofwork']
        referedbydata = request.POST['referedby']
        modeofcontact = request.POST['modeofcontact']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        date = request.POST['date']
        uid = random_string(referedbydata)
        r = Copyright(Categoryofwork=categoryofwork, clientname=clientname, titleofwork=titleofwork,
                      referedby=referedbydata
                      , modeofcontact=modeofcontact, conntactnumber=contactnumber, emailid=emailid, uid=uid, date=date)
        r.save()
        return redirect('home')
    else:
        return render(request, "copyright/Copyrightapplication.html", {'ref': referedby.objects.all,'user':users})


def CopyrightStatusup(r):
    if r.method == "POST":
        uid = r.POST['uid']
        cp = Copyright.objects.get(uid=uid)
        cp.status = True
        cp.save()
    return redirect('user/login')


def delepteAppCopyright(r, uid):
    Copyright.objects.get(uid=uid).delete()
    return redirect('user/login')
