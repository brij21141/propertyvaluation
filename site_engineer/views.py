from django.shortcuts import render, redirect,get_object_or_404
from site_engineer.models import EngineerReport,HistoryEngineerReport,Floordetails,HistoryFloordetails,EngDynamicdValue,HistoryEngDynamicdValue
from reception.models import ReceptionReport,Document
from datetime import datetime
from propval.models import UserDetails,Banks,Impdoc,EngDynamicField
from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect,JsonResponse
from django.conf import settings
import os , requests, time
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.db import transaction
from django.utils.text import slugify

# Create your views here.

def add_report(request,repid):
    with transaction.atomic():  # Start the transaction  if transactions fails it will rollback data
        if request.user.is_authenticated:
            useremail = request.user.email
            userid = User.objects.get(email=useremail)
            if(UserDetails.objects.filter(user_email=useremail).exists()):
                username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
                userrole = UserDetails.objects.get(user_email=useremail).role
                uid = UserDetails.objects.get(user_email=useremail).user_id
        
        try: 
            engdynamicfields=EngDynamicField.objects.exclude(active=False)
        except:
            engdynamicfields=[]
        
        if request.method == "POST":
            # print (request.POST)
            
            app_number = request.POST.get("appno")
            app_name = request.POST.get("name")
            visitinpresence = request.POST.get("presence")
            app_bankname = Banks.objects.get(pk=request.POST.get("bankid")).name
            app_bankid = request.POST.get("bankid")
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
            # barea = request.POST.get("basement")
            # gfarea = request.POST.get("groundfloor")
            # ffarea = request.POST.get("firstfloor")
            # sfarea = request.POST.get("secondfloor")
            # tfarea = request.POST.get("thirdfloor")
            # frarea = request.POST.get("fourthfloor")
            # fvarea = request.POST.get("Fifthfloor")
            # sxarea = request.POST.get("sixthfloor")
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
            er.bankid = app_bankid
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
            # er.barea = barea
            # er.gfarea = gfarea
            # er.ffarea = ffarea
            # er.sfarea = sfarea
            # er.tfarea = tfarea
            # er.frarea = frarea
            # er.fvarea = fvarea
            # er.sxarea = sxarea
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
            er.userdetailsid=userid
            er.receptionid=ReceptionReport.objects.get(pk=repid,applicationnumber=app_number)
            # print(repid)
            # er.priority = ReceptionReport.objects.get(applicationnumber=app_number,pk=repid).priority
            er.save()

            newrecid=er.id
            floorsengid = EngineerReport.objects.get(pk = newrecid)
            # saving floor details
            floors = request.POST.getlist('floor[]')  
            floor_details = request.POST.getlist('floordetails[]')  
            floor_areas = request.POST.getlist('floorarea[]')  
            for i in range(len(floors)):  
                floor_value = floors[i]  
                detail_value = floor_details[i]  
                area_value = floor_areas[i] 

                Floordetails.objects.create(floorname=floor_value, floordetail=detail_value, floorarea=area_value,engreportid = floorsengid)  

            form_data = {}
            for field in engdynamicfields:  
            # Get the submitted value from request.POST  
                field_value = request.POST.get(field.label.replace(' ', '-').lower())  
                form_data[field.label] = field_value  
                EngDynamicdValue.objects.create(input_field=field,value=field_value,engreportid=floorsengid)
            # print (form_data)

            uploaded_files = request.FILES.getlist('engineerFiles') 
            for uploaded_file in uploaded_files:
                # print(time.time())
                newfilename = app_number + "_"+str(newrecid)+'_'+str(time.time())+'_' + uploaded_file.name
                file_path = os.path.join(settings.MEDIA_ROOT,'engineer', newfilename)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                Document.objects.create(
                    application_number=app_number,
                    file_path='engineer/'+newfilename,
                    file_name=newfilename,
                    reception_idno=repid,
                    username=username,
                    role=userrole,
                    usersdetailsid=uid,
                    platform = 'engineer'
                    
                )



            rr=ReceptionReport.objects.get(applicationnumber=app_number,pk=repid)
            rr.engineer='Submitted'
            rr.engid=newrecid
            rr.save()
            # print(request.POST.get("nala"))
            return redirect ('/engineer/engineerhome/')
        # print(repid)
        # receivedrequest=ReceptionReport.objects.all().filter(id=repid).values
        rr=ReceptionReport.objects.get(pk=repid)
        banks= Banks.objects.all().values('id','name','branch','city')
        try:
            response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
        
            if response.status_code == 200:  
                allstates = response.json()  
                states=allstates.get('states')
            else:  
                states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
        except requests.ConnectionError:
            states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
        
        return render(request,"engineer/engineersiteform.html",{'requestreceived':rr,'engdynamicfields':engdynamicfields, 'banks':banks,'states':states})
@login_required(login_url='login')
def engineerhome(request):
    if request.user.is_authenticated:
        useremail = request.user.email
        userid = User.objects.get(email=useremail).id
        user=User.objects.get(username=useremail)
        token , _ = Token.objects.get_or_create(user=user)
    context = {
        'api_base_url': settings.API_BASE_URL,
        'token': str(token)
    }
    if request.method =='POST':
        # messages.success(request, 'This job is in hold status now.')  
        return redirect('/engineer/engineerhome/')
    else:
        if request.user.is_authenticated:
                useremail = request.user.email
                if(UserDetails.objects.filter(user_email=useremail).exists()):
                    username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
                    userrole = UserDetails.objects.get(user_email=useremail).role   
                    if userrole == "Admin":
                            allreport=ReceptionReport.objects.all()
                            receivedrequest=ReceptionReport.objects.exclude(engineer ='Submitted').order_by('-priority','-updated_at')
                            totalrequestnumber = ReceptionReport.objects.count()
                            totalcompleted = ReceptionReport.objects.filter(engineer='Submitted').count()
                            # print(totalrequestnumber-totalcompleted)
                            completedrequest=EngineerReport.objects.all().order_by('-priority','-updated_at')
                            inprogress = ReceptionReport.objects.filter(engineer='InProgress').count()
                            hold = ReceptionReport.objects.filter(engineer='Hold').count()
                            pendingrequest = totalrequestnumber-(totalcompleted+inprogress+hold)
                            
                    else:
                            allreport=ReceptionReport.objects.all()
                            # allreport=ReceptionReport.objects.filter(visitingpersonname=username)
                            receivedrequest=ReceptionReport.objects.exclude(engineer ='Submitted').filter(visitingpersonname=username).order_by('-priority','-updated_at')
                            # totalrequestnumber = ReceptionReport.objects.filter(visitingpersonname=username).count()
                            totalrequestnumber = ReceptionReport.objects.filter(visitingpersonname=username).count()
                            totalcompleted = ReceptionReport.objects.filter(visitingpersonname=username, engineer='Submitted').count()
                            # print(totalrequestnumber-totalcompleted)
                            completedrequest=EngineerReport.objects.filter(receptionid__visitingpersonname=username).order_by('-priority','-updated_at')
                            inprogress = ReceptionReport.objects.filter(visitingpersonname=username, engineer='InProgress').count()
                            hold = ReceptionReport.objects.filter(visitingpersonname=username, engineer='Hold').count()
                            pendingrequest = totalrequestnumber-(totalcompleted+inprogress+hold)
        impdocs= Impdoc.objects.all()                    
        return render(request,"engineer/engineerhome.html",
                {'requestreceived':receivedrequest,
                 'allreports':allreport,
                'totreq':totalrequestnumber,
                'requestcompleted':completedrequest,
                'compreq':totalcompleted,
                'pending':pendingrequest,
                'inprogress':inprogress,
                'hold':hold,
                'context':context,
                'impdocs':impdocs,
                'date':datetime.now()})

def del_report(request,repid,appno):
    # print (repid)
    rr=EngineerReport.objects.get(pk=repid)
    rr.delete()
    rr=ReceptionReport.objects.get(applicationnumber=appno)
    rr.engineer=''
    rr.save()
    return redirect('/engineer/engineerhome/')

def update_report(request,repid):
            
        if request.user.is_authenticated:
            useremail = request.user.email
            if(UserDetails.objects.filter(user_email=useremail).exists()):
                username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
                userrole = UserDetails.objects.get(user_email=useremail).role
                uid = UserDetails.objects.get(user_email=useremail).id
            engdynamicvalues=EngDynamicdValue.objects.filter(engreportid=repid)
            with transaction.atomic():  # Start the transaction  if transactions fails it will rollback data
                if request.method == "POST":
                    app_number = request.POST.get("appno")
                    app_name = request.POST.get("name")
                    visitinpresence = request.POST.get("presence")
                    # app_bankname = request.POST.get("bankname")
                    app_bankname = Banks.objects.get(pk=request.POST.get("bankid")).name
                    app_bankid = request.POST.get("bankid")
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
                    barea = request.POST.get("basement")
                    gfarea = request.POST.get("groundfloor")
                    ffarea = request.POST.get("firstfloor")
                    sfarea = request.POST.get("secondfloor")
                    tfarea = request.POST.get("thirdfloor")
                    frarea = request.POST.get("fourthfloor")
                    fvarea = request.POST.get("Fifthfloor")
                    sxarea = request.POST.get("sixthfloor")
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

                    # retaining existing record
                    old_record = HistoryEngineerReport(  
                    engreport=er,
                    old_id = er.id, 
                    applicationnumber = er.applicationnumber,
                    name = er.name,
                    visitinpresence = er.visitinpresence,
                    bankname = er.bankname,
                    bankid = er.bankid,
                    casetype = er.casetype,
                    add1 = er.add1,
                    add2 = er.add2,
                    city = er.city,
                    region = er.region,
                    zip = er.zip,
                    country = er.country,
                    east = er.east,
                    west = er.west,
                    north = er.north,
                    south = er.south,
                    barea = er.barea,
                    gfarea = er.gfarea,
                    ffarea = er.ffarea,
                    sfarea = er.sfarea,
                    tfarea = er.tfarea,
                    frarea = er.frarea,
                    fvarea = er.fvarea,
                    sxarea = er.sxarea,
                    propertyage = er.propertyage,
                    landrate = er.landrate,
                    Occupant = er.Occupant,
                    landmark = er.landmark,
                    roadwidth = er.roadwidth,
                    hightensionline = er.hightensionline,
                    railwayline = er.railwayline,
                    nala=    er.nala ,
                    river=    er.river,
                    pahad=    er.pahad ,
                    roadcomesunderroadbinding=    er.roadcomesunderroadbinding,
                    propertyaccessissue=    er.propertyaccessissue,
                    othercheck=    er.othercheck,
                    others=er.others,
                    remark = er.remark  
                    )  
                    old_record.save()  
                    oldrecid = old_record.id
                    # copying floor records to history floor records
                    historyengreportid = HistoryEngineerReport.objects.get(pk=oldrecid)
                    floors = Floordetails.objects.filter(engreportid=repid)
                    for floor in floors:
                        old_floor = HistoryFloordetails(  
                        floorname = floor.floorname,
                        floordetail = floor.floordetail,
                        floorarea = floor.floorarea,
                        engreportid = floor.engreportid,
                        historyengreportid = historyengreportid
                        # historyengreportid = HistoryEngineerReport.objects.get(pk=oldrecid)
                        )
                        old_floor.save()
                    # deleting existing floor details and inserting updated 
                    Floordetails.objects.filter(engreportid=repid).delete()
                    floorsengid = EngineerReport.objects.get(pk = repid)
                    # saving floor details
                    floors = request.POST.getlist('floor[]')  
                    floor_details = request.POST.getlist('floordetails[]')  
                    floor_areas = request.POST.getlist('floorarea[]')  
                    for i in range(len(floors)):  
                        floor_value = floors[i]  
                        detail_value = floor_details[i]  
                        area_value = floor_areas[i] 

                        Floordetails.objects.create(floorname=floor_value, floordetail=detail_value, floorarea=area_value,engreportid = floorsengid)      
                    # copying dynamic fields records to history dynamic field records
                    dynamicfields = EngDynamicdValue.objects.filter(engreportid=repid)
                    for dynamic in dynamicfields:
                        old_dynamic = HistoryEngDynamicdValue(  
                        input_field = dynamic.input_field,
                        value = dynamic.value,
                        engreportid = dynamic.engreportid,
                        hsengreportid = historyengreportid
                        )
                        old_dynamic.save()
                    # deleting existing dynamic values details and inserting updated 
                    EngDynamicdValue.objects.filter(engreportid=repid).delete()
                    # floorsengid = EngineerReport.objects.get(pk = repid)
                    # saving dynamic fields details
                    try: 
                        engdynamicfields=EngDynamicField.objects.all()
                    except:
                        engdynamicfields=[]
                    form_data = {}
                    for field in engdynamicfields:  
                    # Get the submitted value from request.POST  
                        field_value = request.POST.get(field.label.replace(' ', '-').lower())  
                        if field_value: 
                            form_data[field.label] = field_value  
                            EngDynamicdValue.objects.create(input_field=field,value=field_value,engreportid=floorsengid)
                                
                    recid=er.receptionid_id
                    er.applicationnumber = app_number
                    er.name = app_name
                    er.visitinpresence = visitinpresence
                    er.bankname = app_bankname
                    er.bankid = app_bankid
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
                    er.barea = barea
                    er.gfarea = gfarea
                    er.ffarea = ffarea
                    er.sfarea = sfarea
                    er.tfarea = tfarea
                    er.frarea = frarea
                    er.fvarea = fvarea
                    er.sxarea = sxarea
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
                    er.edited = True
                    er.save()
                    uploaded_files = request.FILES.getlist('engineerFiles')
                    for uploaded_file in uploaded_files:
                        newfilename = f"{app_number}_{str(repid)}_{str(time.time())}_{uploaded_file.name}"
                        file_path = os.path.join(settings.MEDIA_ROOT,'engineer/', newfilename)

                        try:
                            existing_doc = Document.objects.get(application_number=app_number, file_name=newfilename,reception_idno=repid)
                            os.remove(existing_doc.file_path)
                            existing_doc.delete()
                        except Document.DoesNotExist:
                            pass

                        with default_storage.open(file_path, 'wb+') as destination:
                            for chunk in uploaded_file.chunks():
                                destination.write(chunk)
                    
                        Document.objects.create(
                            application_number=app_number,
                            file_path='engineer/'+newfilename,
                            file_name=newfilename,
                            reception_idno=recid,
                            username=username,
                            role=userrole,
                            usersdetailsid=uid,
                            platform = 'engineer'
                        )

                    return redirect ('/engineer/engineerhome/')
        rr=EngineerReport.objects.get(pk=repid)
        recid=rr.receptionid_id
        # print(recid)
        # appdate=rr.applicationdate.strftime("%Y-%m-%d")
        documents = Document.objects.filter(application_number=rr.applicationnumber,reception_idno=recid, platform = 'engineer')
        banks= Banks.objects.all().values('id','name','branch','city')
        floors = Floordetails.objects.filter(engreportid_id=repid)
        try:
            response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
        
            if response.status_code == 200:  
                allstates = response.json()  
                states=allstates.get('states')
            else:  
                states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
        except requests.ConnectionError:
            states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
        return render(request,'engineer/engineersiteform.html',{'recptreport':rr,'engdynamicvalues':engdynamicvalues, 'documents':documents,'banks':banks,'states':states,'floors':floors})

def delete_file(request, doc_id):
    try:
        document = Document.objects.get(pk=doc_id)
        # os.remove(document.file_path)
        os.remove(os.path.join(settings.MEDIA_ROOT,document.file_path))
        document.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return JsonResponse({  
        'message': 'File deleted',  
        'redirect': request.META.get('HTTP_REFERER', '/')  
        })
    except Document.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Document does not exist'})


