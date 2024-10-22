from django.shortcuts import render,redirect
from site_engineer.models import EngineerReport
from reception.models import ReceptionReport
from datetime import datetime
from propval.models import UserDetails
# Create your views here.

def add_report(request,repid):
    if request.method == "POST":
        app_number = request.POST.get("appno")
        app_name = request.POST.get("name")
        visitinpresence = request.POST.get("presence")
        app_bankname = request.POST.get("bankname")
        casetype = request.POST.get("case")
        app_add1 = request.POST.get("add1")
        app_add2 = request.POST.get("add2")
        app_city = request.POST.get("city")
        app_region = request.POST.get("region")
        app_zip = request.POST.get("zip")
        app_country = request.POST.get("country")
        eastboundary = request.POST.get("east")
        westboundary = request.POST.get("west")
        northboundary = request.POST.get("north")
        southboundary = request.POST.get("south")
        gfarea = request.POST.get("groundfloor")
        ffarea = request.POST.get("firstfloor")
        sfarea = request.POST.get("secondfloor")
        tfarea = request.POST.get("thirdfloor")
        propertyage = request.POST.get("age")
        landrate = request.POST.get("rate")
        occupant = request.POST.get("occupant")
        lanrented = request.POST.get("ranted")
        landmark = request.POST.get("landmark")
        roadwidth = request.POST.get("roadwidth")
        hightension = request.POST.get("hightension")
        railwayline = request.POST.get("railwayline")
        nala = request.POST.get("nala")
        river = request.POST.get("river")
        pahad = request.POST.get("pahad")
        roadbinding = request.POST.get("roadbinding")
        accessissue = request.POST.get("accessissue")
        otherhazard = request.POST.get("otherhazard")
        otherhazarddesc = request.POST.get("otherhazarddesc")
        remark = request.POST.get("remark")

        er=EngineerReport()
        er.applicationnumber = app_number
        er.name = app_name
        er.visitinpresence = visitinpresence
        er.bankname = app_bankname
        er.casetype = casetype
        er.add1 = app_add1
        er.add2 = app_add2
        er.city = app_city
        er.region = app_region
        er.zip = app_zip
        er.country = app_country
        er.east = eastboundary
        er.west = westboundary
        er.north = northboundary
        er.south = southboundary
        er.gfarea = gfarea
        er.ffarea = ffarea
        er.sfarea = sfarea
        er.tfarea = tfarea
        er.propertyage = propertyage
        er.landrate = landrate
        er.Occupant = occupant
        er.landmark = landmark
        er.roadwidth = roadwidth
        if hightension is None:
            er.hightensionline = False
        else:
            er.hightensionline = True
        if railwayline is None:
            er.railwayline = False
        else:
            er.railwayline = True
        if nala is None:
            er.nala = False
        else:
            er.nala = True
        if river is None:
            er.river = False
        else:
            er.river = True
        if pahad is None:
            er.pahad = False
        else:
            er.pahad = True
        if roadbinding is None:
            er.roadcomesunderroadbinding = False
        else:
            er.roadcomesunderroadbinding = True
        if accessissue is None:
            er.propertyaccessissue = False
        else:
            er.propertyaccessissue = True
        if otherhazard is None:
            er.othercheck = False
        else:
            er.othercheck = True
        er.others = otherhazarddesc
        er.remark = remark
        er.save()
        rr=ReceptionReport.objects.get(applicationnumber=app_number)
        rr.engineer='Submitted'
        rr.save()
        # print(request.POST.get("nala"))
        return redirect ('/engineer/engineerhome/')
    # print(repid)
    # receivedrequest=ReceptionReport.objects.all().filter(id=repid).values
    rr=ReceptionReport.objects.get(pk=repid)
    return render(request,"engineer/engineersiteform.html",{'requestreceived':rr})

def reporterhome(request):
    # receivedrequest=ReceptionReport.objects.all()
    if request.user.is_authenticated:
        useremail = request.user.email
        username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
    # print(username)
    receivedrequest=EngineerReport.objects.exclude(engineer ='Submitted')
    # totalrequestnumber = ReceptionReport.objects.filter(visitingpersonname=username).count()
    totalrequestnumber = ReceptionReport.objects.count()
    completedrequest=EngineerReport.objects.all()
    totalcompleted = ReceptionReport.objects.filter(visitingperson__gt=1, engineer='Submitted').count()
    pendingrequest = totalrequestnumber-totalcompleted
    # print(totalrequestnumber-totalcompleted)
    inprogress = ReceptionReport.objects.filter(visitingperson__gt=1, engineer='InProgress').count()
    hold = ReceptionReport.objects.filter(visitingperson__gt=1, engineer='Hold').count()
    return render(request,"reporter/reporterhome.html",
                  {'requestreceived':receivedrequest,
                   'totreq':totalrequestnumber,
                   'requestcompleted':completedrequest,
                   'compreq':totalcompleted,
                   'pending':pendingrequest,
                   'inprogress':inprogress,
                   'hold':hold,
                   'date':datetime.now()})
    # return render(request,"engineer/engineerhome.html",{'requestreceived':receivedrequest})

def del_report(request,repid,appno):
    # print (repid)
    rr=EngineerReport.objects.get(pk=repid)
    rr.delete()
    rr=ReceptionReport.objects.get(applicationnumber=appno)
    rr.engineer=''
    rr.save()
    return redirect('/engineer/engineerhome/')

def update_report(request,repid):
    if request.method == "POST":
        app_number = request.POST.get("appno")
        app_name = request.POST.get("name")
        visitinpresence = request.POST.get("presence")
        app_bankname = request.POST.get("bankname")
        casetype = request.POST.get("case")
        app_add1 = request.POST.get("add1")
        app_add2 = request.POST.get("add2")
        app_city = request.POST.get("city")
        app_region = request.POST.get("region")
        app_zip = request.POST.get("zip")
        app_country = request.POST.get("country")
        eastboundary = request.POST.get("east")
        westboundary = request.POST.get("west")
        northboundary = request.POST.get("north")
        southboundary = request.POST.get("south")
        gfarea = request.POST.get("groundfloor")
        ffarea = request.POST.get("firstfloor")
        sfarea = request.POST.get("secondfloor")
        tfarea = request.POST.get("thirdfloor")
        propertyage = request.POST.get("age")
        landrate = request.POST.get("rate")
        occupant = request.POST.get("occupant")
        lanrented = request.POST.get("ranted")
        landmark = request.POST.get("landmark")
        roadwidth = request.POST.get("roadwidth")
        hightension = request.POST.get("hightension")
        railwayline = request.POST.get("railwayline")
        nala = request.POST.get("nala")
        river = request.POST.get("river")
        pahad = request.POST.get("pahad")
        roadbinding = request.POST.get("roadbinding")
        accessissue = request.POST.get("accessissue")
        otherhazard = request.POST.get("otherhazard")
        otherhazarddesc = request.POST.get("otherhazarddesc")
        remark = request.POST.get("remark")
        
        er=EngineerReport.objects.get(pk=repid)
        # rr.applicationdate=app_date
        er.applicationnumber = app_number
        er.name = app_name
        er.visitinpresence = visitinpresence
        er.bankname = app_bankname
        er.casetype = casetype
        er.add1 = app_add1
        er.add2 = app_add2
        er.city = app_city
        er.region = app_region
        er.zip = app_zip
        er.country = app_country
        er.east = eastboundary
        er.west = westboundary
        er.north = northboundary
        er.south = southboundary
        er.gfarea = gfarea
        er.ffarea = ffarea
        er.sfarea = sfarea
        er.tfarea = tfarea
        er.propertyage = propertyage
        er.landrate = landrate
        er.Occupant = occupant
        er.landmark = landmark
        er.roadwidth = roadwidth
        if hightension is None:
            er.hightensionline = False
        else:
            er.hightensionline = True
        if railwayline is None:
            er.railwayline = False
        else:
            er.railwayline = True
        if nala is None:
            er.nala = False
        else:
            er.nala = True
        if river is None:
            er.river = False
        else:
            er.river = True
        if pahad is None:
            er.pahad = False
        else:
            er.pahad = True
        if roadbinding is None:
            er.roadcomesunderroadbinding = False
        else:
            er.roadcomesunderroadbinding = True
        if accessissue is None:
            er.propertyaccessissue = False
        else:
            er.propertyaccessissue = True
        if otherhazard is None:
            er.othercheck = False
        else:
            er.othercheck = True
        er.others = otherhazarddesc
        er.remark = remark
        er.save()
        return redirect ('/engineer/engineerhome/')
    rr=EngineerReport.objects.get(pk=repid)
    # appdate=rr.applicationdate.strftime("%Y-%m-%d")
    return render(request,'engineer/engineersiteform.html',{'recptreport':rr})


