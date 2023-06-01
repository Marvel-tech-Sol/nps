import random

from django.apps import apps
from django.shortcuts import render, redirect
from .models import Design

# Create your views here.
def random_string(ReferedBy):
    unique_id = ReferedBy[0:2] + "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    return unique_id

def Designapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        categoryofwork = request.POST['categoryofwork']
        clientname = request.POST['clientname']
        titleofwork = request.POST['titleofwork']
        modeofcontact = request.POST['modeofcontact']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        date = request.POST['date']
        uid = random_string(referedby)
        r = Design(categoryofwork=categoryofwork, clientname=clientname, titleofwork=titleofwork, modeofcontact=modeofcontact, referedBy=referedby
                                  , contactnumber=contactnumber, email=emailid,date=date,uid=uid)
        r.save()
        return redirect('users/login')
    else:
         return render(request,"Design/Designapplication.html",{'ref':referedby.objects.all})

def Designtableview(r):
    c = Design.objects.all()
    return render(r,"Design/Designtable.html",{'c':c})

def Designstatusview(r,uid):
    design= Design.objects.get(uid = uid)
    return render(r,"Design/Designstatus.html",{'des':design})