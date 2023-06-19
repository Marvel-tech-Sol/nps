import random

from django.apps import apps
from django.shortcuts import render, redirect
from .models import Patentapplication, NDAStatus, PaymentStatus, NoveltyStatus, DocumentationStatus, DrawingStatus, \
    DraftingStatus, FerStatus, ExaminationSatus, FilingStatus, HearingStatus, GrantsStatus, Assignedto


def random_string(ReferedBy):
    unique_id = ReferedBy[0:2] + "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    return unique_id


# Create your views here.
def FullPatentapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    users = apps.get_model('login', 'Usermodel').objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        modeofcontact = request.POST['modeofcontact']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        uid = random_string(referedby)
        date = request.POST['date']
        nda = request.POST['ndastatus']
        idf = request.POST['idfstatus']
        quotation = request.POST['quastatus']
        assignto = request.POST['assignto']
        r = Patentapplication(title=title, uid=uid, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact,
                              patenttype='full', status=False, date=date, nda=nda, idf=idf, qua=quotation)
        r.save()
        NDAStatus(uid=uid, status=True, nda=nda).save()
        NoveltyStatus(uid=uid, status=False).save()
        DraftingStatus(uid=uid, status=False).save()
        DrawingStatus(uid=uid, status=False).save()
        DocumentationStatus(uid=uid, status=False).save()
        FilingStatus(uid=uid, status=False).save()
        ExaminationSatus(uid=uid, status=False).save()
        FerStatus(uid=uid, status=False).save()
        HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        Assignedto(uid=uid, assignstatus=True, assignto=assignto).save()
        return redirect('home')
    return render(request, "Patent/FullPatentapplication.html", {'ref': referedby.objects.all, 'user': users})


def Patentapplicationview(request):
    users = apps.get_model('login', 'Usermodel').objects.all()
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        title = request.POST['title']
        type = request.POST['check[]']
        organization = request.POST['organization']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        modeofcontact = request.POST['modeofcontact']
        assignto = request.POST['assignto']
        nda = request.POST['ndastatus']
        idf = request.POST['idfstatus']
        quotation = request.POST['quastatus']
        uid = random_string(referedby)
        date = request.POST['date']
        r = Patentapplication(uid=uid, title=title, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact, date=date,
                              patenttype=type, nda=nda, idf=idf, qua=quotation)
        r.save()
        NDAStatus(uid=uid, status=True, nda=nda).save()
        if type == 'novelty search':
            NoveltyStatus(uid=uid, status=False).save()
        if type == 'drafting':
            DraftingStatus(uid=uid, status=False).save()
        if type == 'drawing':
            DrawingStatus(uid=uid, status=False).save()
        if type == 'documentation':
            DocumentationStatus(uid=uid, status=False).save()
        if type == 'filing':
            FilingStatus(uid=uid, status=False).save()
        if type == 'examination':
            ExaminationSatus(uid=uid, status=False).save()
        if type == 'FER':
            FerStatus(uid=uid, status=False).save()
        if type == 'hearing':
            HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        Assignedto(uid=uid, assignstatus=True, assignto=assignto).save()
        return redirect('home')
    else:
        return render(request, "Patent/Patentapplication.html", {'ref': referedby.objects.all, 'user': users})


def Documentationstatusview(r, uid):
    documentationstatus = Patentapplication.objects.get(uid=uid, patenttype='documentation')

    return render(r, "Patent/Documentationstatus.html", {'c': documentationstatus})


def Documentationtableview(r):
    return render(r, "Patent/Documentationtable.html")


def Draftingstatusview(r, uid):
    draftingstatus = Patentapplication.objects.get(uid=uid)
    draftstatus =DraftingStatus.objects.get(uid=uid)
    return render(r, "Patent/Draftingstatus.html", {'c': draftingstatus,'draftstatus':draftstatus})


def Draftingtableview(r):
    return render(r, "Patent/Draftingtable.html")


def Drawingstatusview(r, uid):
    drawingstatus = Patentapplication.objects.get(uid=uid)
    return render(r, "Patent/Drawingstatus.html", {'c': drawingstatus})


def Drawingtableview(r):
    return render(r, "Patent/Drawingtable.html")


def Patentabilitysearchstatusview(r, uid):
    patentabilitysearchstatus = Patentapplication.objects.get(uid=uid)
    NoveltyStatus = apps.get_model('Patent', 'NoveltyStatus')
    return render(r, "Patent/Patentabilitysearchstatus.html",
                  {'c': patentabilitysearchstatus, 'NoveltyStatus': NoveltyStatus.objects.get(uid=uid)})


def Patentabilitysearchtableview(r):
    return render(r, "Patent/Patentabilitysearchtable.html")


def Drawingstatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        r = DrawingStatus.objects.get(uid=uid)
        r.status = True
        r.save()
        return redirect('user/login')


def Documentationstatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        r = DocumentationStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')


def Draftingstatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        dr = DraftingStatus.objects.get(uid=uid)
        dr.status = True
        dr.duedate = r.POST['duedate']
        dr.assignto = r.POST['assignto']
        dr.rating=r.POST['rating']
        dr.qc = r.POST['qc']
        dr.drawings = r.POST['drawings']
        dr.save()
    return redirect('user/login')


def GrantsStatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        r = GrantsStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')


def FilingStatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        r = FilingStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')


def ExaminationSatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        r = ExaminationSatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')


def FerStatusdata(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        fer = FerStatus.objects.get(uid=uid)
        fer.status = True
        fer.duedate = r.POST['duedate']
        fer.assignto = r.POST['assignto']
        fer.rating = r.POST['rating']
        fer.qc = r.POST['qc']
        fer.save()
    return redirect('user/login')


def FerstatusView(r,uid):
    Fer = FerStatus.objects.get(uid=uid)
    patent = Patentapplication.objects.get(uid=uid)
    return render(r,'Patent/Ferstatus.html',{'Fer':Fer,'c':patent})


def Patentabilitysearchstatusdata(r):
    if r.method == "POST":
        uid = r.POST['uid']
        duedate = r.POST['duedate']
        assignto = r.POST['assignto']
        rating=r.POST['rating']
        qc = r.POST['qc']
        n = NoveltyStatus.objects.get(uid=uid)
        n.status = True
        n.duedate = duedate
        n.rating = rating
        n.qc = qc
        n.assignto = assignto
        n.save()
        return redirect('user/login')
    return redirect('user/login')


def Hearingstatusdata(r):
    if r.method == "POST":
        uid = r.POST['uid']
        date = r.POST['date']
        n = HearingStatus.objects.get(uid=uid)
        n.status = True
        n.date = date
        n.save()
        return redirect('user/login')

    return redirect('user/login')


def paymentStatus(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        amount = r.POST['amount']
        p = PaymentStatus.objects.get(uid=uid)
        p.status = True
        p.amount = amount
        p.save()
    return redirect('user/login')

def approvenovelty(r,uid):
    n = NoveltyStatus.objects.get(uid=uid)
    n.approved = True
    n.save()
    return redirect('user/login')

def reassignnovelty(r,uid):
    n = NoveltyStatus.objects.get(uid=uid)
    n.status = False
    n.save()
    return redirect('user/login')

def approvedraft(r,uid):
    dr = DraftingStatus.objects.get(uid=uid)
    dr.approved = True
    dr.save()
    return redirect('user/login')

def reassigndraft(r,uid):
    dr = DraftingStatus.objects.get(uid=uid)
    dr.status = False
    dr.save()
    return redirect('user/login')

def approvefer(r,uid):
    dr = FerStatus.objects.get(uid=uid)
    dr.approved = True
    dr.save()
    return redirect('user/login')

def reassignfer(r,uid):
    dr = FerStatus.objects.get(uid=uid)
    dr.status = False
    dr.save()
    return redirect('user/login')