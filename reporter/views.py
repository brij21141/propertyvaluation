from django.shortcuts import render,redirect
import googlemaps.client
from site_engineer.models import EngineerReport
from reception.models import ReceptionReport, Document
from reporter.models import ReporterReport
from datetime import datetime
from propval.models import UserDetails
from django.db.models import Q
from django.contrib.auth.models import User
from django.views import View
import googlemaps
from django.conf import settings
from django.core.files.storage import default_storage
from propval.models import Banks
import os
# Create your views here.

def add_report(request,repid):
    er=EngineerReport.objects.get(pk=repid)
    if request.user.is_authenticated:
        useremail = request.user.email
        userid = User.objects.get(email=useremail)
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).user_id

    if request.method == "POST":
        
        rre=request.POST
        # print(rre['appno'])
        # print(rre['propertytype'])
        # print(er.receptionid_id)
        # print(er.receptionid)
        rr=ReporterReport()
        rr.applicationnumber = rre['appno']
        rr.inspectiondate = rre['inspdate']
        rr.name=rre['custname']
        rr.docholdername=rre['dname']
        rr.propertytype=rre['propertytype']
        rr.add1=rre['add1']
        rr.add2=rre['add2']
        rr.city=rre['city']
        rr.region=rre['region']
        rr.zip=rre['zip']
        rr.country=rre['country']
        rr.landmark=rre['landmark']
        rr.ladd1=rre['ladd1']
        rr.ladd2=rre['ladd2']
        rr.lcity=rre['lcity']
        rr.lregion=rre['lregion']
        rr.lzip=rre['lzip']
        rr.lcountry=rre['lcountry']
        rr.wardlandno=rre['ward']
        rr.approachroadwidth=rre['aroadwidth']
        rr.plotdem=rre['plotds']
        rr.vicinity=rre['vicinity']
        rr.propertylocation=rre['proplocation']
        rr.propertyidentification=rre['propident']
        rr.connectivityinfrastructure=rre['connectivity']
        rr.railwaystation=rre['rly']
        rr.busstop=rre['bus']
        rr.hospital=rre['hosp']
        rr.nearestlandmark=rre['nlandmark']
        rr.typeusageproperty=rre['usagetype']
        rr.additionalamenities=rre['addaminity']
        rr.legalstatusproperty=rre['lsp']
        rr.typepremises=rre['permissiontype']
        rr.taxationmaintancecost=rre['taxation']

        rr.rentingpotential=rre['rentedpotential']
        rr.marketrentals=rre['mktrental']
        rr.occupiedby=rre['occupiedby']
        rr.ispropertyrented=rre['rentedproperty']
        rr.listofoccupants=rre['roadwidth']
        rr.perdcboundryeast=rre['eastboundary']
        rr.perstboundrywest=rre['westboundary']
        rr.perdcboundrynorth=rre['northboundary']
        rr.perdcboundrysouth=rre['southboundar']

        rr.perstboundryeast=rre['seastboundary']
        rr.perstboundrywest=rre['swestboundary']
        rr.perstboundrynorth=rre['snorthboundary']
        rr.perstboundrysouth=rre['ssouthboundary']

        rr.typestructure=rre['structtype']
        rr.nofloors=rre['nofloor']
        rr.nowings=rre['wingsno']
        rr.nouniteachfloor=rre['flunitno']
        rr.nolifteachwing=rre['wingliftno']
        rr.ageproperty=rre['propertyage']
        rr.futurelife=rre['estfutlife']
        rr.exterior=rre['exteriors']
        rr.internalcomposition=rre['propcomsition']
        rr.constructionquality=rre['constqualty']
        rr.beamcolumnstru=rre['clmstruct']
        rr.commonarearemark=rre['commremarks']
        rr.otherobservation=rre['otherobsr']
        rr.floornfinish=rre['interrfinish']
        rr.roofingnterracing=rre['roofterr']
        rr.nooflifts=rre['nolifts']
        rr.qualityfixing=rre['qltfix']
        rr.constasperaprove=rre['consancplan']
        rr.aprnodate=rre['apvnodate']
        rr.constnodate=rre['consperdate']
        rr.violationifany=rre['violrisk']
        rr.confirmlocalbilaws=rre['lclbilaw']
        rr.otherverifieddoc=rre['docverified']
        rr.carpetareaflwise=rre['cafw']
        rr.aprovbuaflwise=rre['apbuaflw']
        rr.govtapprovalrate=rre['cgarate']
        rr.recomendrate=rre['recmdrate']
        rr.mktvalueinfig=rre['fmvrsinfig']
        rr.mktvalueinwords=rre['fmvrsinwords']
        rr.forcessalesless=rre['fslless']
        rr.arearatepsft=rre['fsratepsqf']
        rr.areavalueinfig=rre['amountinfig']
        rr.areavalueinwords=rre['amountinwrods']
        rr.landarea=rre['landarea']
        rr.govtaprovelandrate=rre['fgarate']
        rr.recommendedlandrate=rre['recomndrate']
        rr.landvalue=rre['landrate']
        rr.actualbua=rre['actbua']
        rr.asperpermissionbua=rre['buaasapprov']
        rr.constcostperaminity=rre['costameniti']
        rr.totalconstvalue=rre['aprovval']
        rr.depreciatedconstvalue=rre['depval']
        rr.landvaluedepndepconstvalueinfig=rre['drpsa']
        rr.landvaluedepndepconstvalueinword=rre['drpsw']
        rr.forcesalevaluepersqft=rre['fratepsqf']
        rr.forcesvalueinfig=rre['frpsa']
        rr.forcesvalueinword=rre['frpsw']
        rr.marketibility=rre['mkt']
        rr.valuationresult=rre['valueresult']
        rr.userdetailsid=userid
        rr.receptionid=ReceptionReport.objects.get(pk=er.receptionid_id,applicationnumber=rre['appno']) 
        rr.bankid=Banks.objects.get(pk = ReceptionReport.objects.get(pk=er.receptionid_id,applicationnumber=rre['appno']).bankid ) 
        # print(ReceptionReport.objects.get(pk=er.receptionid_id,applicationnumber=rre['appno']).bankid)
        # return False
        rr.remark = rre['remark']
        # Geo lat long and place id
        if(rre['add1'] and rre['city'] and rre['region'] and rre['country']  and rre['zip'] != None):
                address_string = str(rre['add1'])+','+str(rre['add2'])+','+str(rre['region'])+','+str(rre['city'])+','+str(rre['country'])+','+str(rre['landmark'])+',',str(rre['zip'])
                gmap =  googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
                result = gmap.geocode(address_string)[0]

                rr.lat = result.get('geometry',{}).get('location',{}).get('lat',None)
                rr.lng = result.get('geometry',{}).get('location',{}).get('lng',None)
                rr.placeid = result.get('place_id',{})


        rr.save()

        newrecid=rr.id
        uploaded_files = request.FILES.getlist('reporterFiles') 
        for uploaded_file in uploaded_files:
            newfilename = rre['appno'] + "_"+str(newrecid)+"_" + uploaded_file.name
            file_path = os.path.join(settings.MEDIA_ROOTREPORTER, newfilename)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            Document.objects.create(
                application_number=rre['appno'],
                file_path=file_path,
                file_name=newfilename,
                reception_idno=er.receptionid_id,
                username=username,
                role=userrole,
                usersdetailsid=uid,
                platform = 'reporter'
                
            )

        rr=ReceptionReport.objects.get(applicationnumber=rre['appno'],pk=er.receptionid_id)
        rr.reporter='Submitted'
        rr.save()
        rr=EngineerReport.objects.get(applicationnumber=rre['appno'],pk=repid)
        rr.reporter='Submitted'
        rr.save()
        
        # print(request.POST.get("nala"))
        return redirect ('/reporter/reporterhome/')
    # print(repid)
    # receivedrequest=ReceptionReport.objects.all().filter(id=repid).values
    
    return render(request,"reporter/reporterform.html",{'requestreceived':er})

def reporterhome(request):
    if request.method =='POST':
         rre=request.POST
        #  print(rre)
        #  print(rre["urlid"])
        #  print(request.POST.get("reporterholdcause"))
         rer=EngineerReport.objects.get(pk=rre["urlid"])
         rr=ReceptionReport.objects.get(pk=rer.receptionid.id)
        #  print ("name-",rr.name)
         rer.reporterholdcause=rre["reporterholdcause"]
         rer.save()
         rr.reporterholdcause=rre["reporterholdcause"]
         rr.save()
         return redirect ('/reporter/reporterhome/')
    if request.user.is_authenticated:
        useremail = request.user.email
        userid = User.objects.get(email=useremail).id
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).id   
            # print(username)
            # results = ReceptionReport.objects.filter(visitingpersonname=username).values('engineer').annotate(count=Count('id'))
            # print(results)
            if userrole == "Admin":
                #   receivedrequest=ReceptionReport.objects.filter(engineer ='Submitted')
                #   receivedrequest=EngineerReport.objects.filter(receptionid__engineer='Submitted')
                  allreport=EngineerReport.objects.all()
                  receivedrequest=EngineerReport.objects.exclude(reporter ='Submitted')
                  print(receivedrequest)
                  completedrequest=ReporterReport.objects.all()
                #   print(EngineerReport.objects.get(pk=13).userdetailsid.first_name)
                  totalrequestnumber = EngineerReport.objects.count()
                  totalcompleted = EngineerReport.objects.filter(reporter='Submitted').count()
                  inprogress = EngineerReport.objects.filter(reporter='InProgress').count()
                  pendingrequest = totalrequestnumber-(totalcompleted+inprogress)
                  hold = EngineerReport.objects.filter(reporter='Hold').count()
            else:
                  allreport=EngineerReport.objects.filter(Q(receptionid__reportperson=userid) | Q(receptionid__reportperson=0))
                  receivedrequest=EngineerReport.objects.exclude(reporter ='Submitted').filter(Q(receptionid__reportperson=userid) | Q(receptionid__reportperson=0))
                  completedrequest=ReporterReport.objects.filter(receptionid__reportperson=userid)
                  totalrequestnumber = EngineerReport.objects.filter(receptionid__reportperson=userid).count()
                  totalcompleted = EngineerReport.objects.filter(receptionid__reportperson=userid, reporter='Submitted').count()
                  inprogress = EngineerReport.objects.filter(receptionid__reportperson=userid, reporter='InProgress').count()
                  pendingrequest = totalrequestnumber-(totalcompleted+inprogress)
                  hold = EngineerReport.objects.filter(receptionid__reportperson=userid, reporter='Hold').count()


    # # receivedrequest=ReceptionReport.objects.all()
    # if request.user.is_authenticated:
    #     useremail = request.user.email
    #     if(UserDetails.objects.filter(user_email=useremail ).exists()):
    #         username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
    # # print(username)
    # receivedrequest=EngineerReport.objects.exclude(reporter ='Submitted')
    # # totalrequestnumber = ReceptionReport.objects.filter(visitingpersonname=username).count()
    # totalrequestnumber = EngineerReport.objects.count()
    # # completedrequest=ReporterReport.objects.all()
    # totalcompleted = EngineerReport.objects.filter(receptionid__visitingperson__gt=1, reporter='Submitted').count()
    # pendingrequest = totalrequestnumber-totalcompleted
    # # print(totalrequestnumber-totalcompleted)
    # inprogress = EngineerReport.objects.filter(receptionid__visitingperson__gt=1, reporter='InProgress').count()
    # hold = EngineerReport.objects.filter(receptionid__visitingperson__gt=1, reporter='Hold').count()
    
    return render(request,"reporter/reporterhome.html",
                  {'requestreceived':receivedrequest,
                   'allreports':allreport,
                   'totreq':totalrequestnumber,
                   'requestcompleted':completedrequest,
                   'compreq':totalcompleted,
                   'pending':pendingrequest,
                   'inprogress':inprogress,
                   'hold':hold,
                   'date':datetime.now()})
    # return render(request,"engineer/engineerhome.html",{'requestreceived':receivedrequest})

# def del_report(request,repid,appno):
#     # print (repid)
#     rr=EngineerReport.objects.get(pk=repid)
#     rr.delete()
#     rr=ReceptionReport.objects.get(applicationnumber=appno)
#     rr.engineer=''
#     rr.save()
#     return redirect('/engineer/engineerhome/')

def update_report(request,repid):

    if request.user.is_authenticated:
        useremail = request.user.email
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).id
    if request.method == "POST":
        
        rre=request.POST
        # print(rre['appno'])
        # print(rre['propertytype'])
        rr=ReporterReport.objects.get(pk=repid)
        rr.applicationnumber = rre['appno']
        rr.inspectiondate = rre['inspdate']
        rr.name=rre['custname']
        rr.docholdername=rre['dname']
        rr.propertytype=rre['propertytype']
        rr.add1=rre['add1']
        rr.add2=rre['add2']
        rr.city=rre['city']
        rr.region=rre['region']
        rr.zip=rre['zip']
        rr.country=rre['country']
        rr.landmark=rre['landmark']
        rr.ladd1=rre['ladd1']
        rr.ladd2=rre['ladd2']
        rr.lcity=rre['lcity']
        rr.lregion=rre['lregion']
        rr.lzip=rre['lzip']
        rr.lcountry=rre['lcountry']
        rr.wardlandno=rre['ward']
        rr.approachroadwidth=rre['aroadwidth']
        rr.plotdem=rre['plotds']
        rr.vicinity=rre['vicinity']
        rr.propertylocation=rre['proplocation']
        rr.propertyidentification=rre['propident']
        rr.connectivityinfrastructure=rre['connectivity']
        rr.railwaystation=rre['rly']
        rr.busstop=rre['bus']
        rr.hospital=rre['hosp']
        rr.nearestlandmark=rre['nlandmark']
        rr.typeusageproperty=rre['usagetype']
        rr.additionalamenities=rre['addaminity']
        rr.legalstatusproperty=rre['lsp']
        rr.typepremises=rre['permissiontype']
        rr.taxationmaintancecost=rre['taxation']

        rr.rentingpotential=rre['rentedpotential']
        rr.marketrentals=rre['mktrental']
        rr.occupiedby=rre['occupiedby']
        rr.ispropertyrented=rre['rentedproperty']
        rr.listofoccupants=rre['roadwidth']
        rr.perdcboundryeast=rre['eastboundary']
        rr.perstboundrywest=rre['westboundary']
        rr.perdcboundrynorth=rre['northboundary']
        rr.perdcboundrysouth=rre['southboundar']

        rr.perstboundryeast=rre['seastboundary']
        rr.perstboundrywest=rre['swestboundary']
        rr.perstboundrynorth=rre['snorthboundary']
        rr.perstboundrysouth=rre['ssouthboundary']

        rr.typestructure=rre['structtype']
        rr.nofloors=rre['nofloor']
        rr.nowings=rre['wingsno']
        rr.nouniteachfloor=rre['flunitno']
        rr.nolifteachwing=rre['wingliftno']
        rr.ageproperty=rre['propertyage']
        rr.futurelife=rre['estfutlife']
        rr.exterior=rre['exteriors']
        rr.internalcomposition=rre['propcomsition']
        rr.constructionquality=rre['constqualty']
        rr.beamcolumnstru=rre['clmstruct']
        rr.commonarearemark=rre['commremarks']
        rr.otherobservation=rre['otherobsr']
        rr.floornfinish=rre['interrfinish']
        rr.roofingnterracing=rre['roofterr']
        rr.nooflifts=rre['nolifts']
        rr.qualityfixing=rre['qltfix']
        rr.constasperaprove=rre['consancplan']
        rr.aprnodate=rre['apvnodate']
        rr.constnodate=rre['consperdate']
        rr.violationifany=rre['violrisk']
        rr.confirmlocalbilaws=rre['lclbilaw']
        rr.otherverifieddoc=rre['docverified']
        rr.carpetareaflwise=rre['cafw']
        rr.aprovbuaflwise=rre['apbuaflw']
        rr.govtapprovalrate=rre['cgarate']
        rr.recomendrate=rre['recmdrate']
        rr.mktvalueinfig=rre['fmvrsinfig']
        rr.mktvalueinwords=rre['fmvrsinwords']
        rr.forcessalesless=rre['fslless']
        rr.arearatepsft=rre['fsratepsqf']
        rr.areavalueinfig=rre['amountinfig']
        rr.areavalueinwords=rre['amountinwrods']
        rr.landarea=rre['landarea']
        rr.govtaprovelandrate=rre['fgarate']
        rr.recommendedlandrate=rre['recomndrate']
        rr.landvalue=rre['landrate']
        rr.actualbua=rre['actbua']
        rr.asperpermissionbua=rre['buaasapprov']
        rr.constcostperaminity=rre['costameniti']
        rr.totalconstvalue=rre['aprovval']
        rr.depreciatedconstvalue=rre['depval']
        rr.landvaluedepndepconstvalueinfig=rre['drpsa']
        rr.landvaluedepndepconstvalueinword=rre['drpsw']
        rr.forcesalevaluepersqft=rre['fratepsqf']
        rr.forcesvalueinfig=rre['frpsa']
        rr.forcesvalueinword=rre['frpsw']
        rr.marketibility=rre['mkt']
        rr.valuationresult=rre['valueresult']
        rr.remark = rre['remark']
        # Geo data lat, long, placeid
        if(rre['add1'] and rre['city'] and rre['region'] and rre['country']  and rre['zip'] != None):
                address_string = str(rre['add1'])+','+str(rre['add2'])+','+str(rre['region'])+','+str(rre['city'])+','+str(rre['country'])+','+str(rre['landmark'])+',',str(rre['zip'])
                gmap =  googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
                result = gmap.geocode(address_string)[0]

                rr.lat = result.get('geometry',{}).get('location',{}).get('lat',None)
                rr.lng = result.get('geometry',{}).get('location',{}).get('lng',None)
                rr.placeid = result.get('place_id',{})


        rr.save()

        uploaded_files = request.FILES.getlist('reporterFiles')
        for uploaded_file in uploaded_files:
            newfilename = f"{rr.applicationnumber}_{str(repid)}_{uploaded_file.name}"
            file_path = os.path.join(settings.MEDIA_ROOTREPORTER, newfilename)

            try:
                existing_doc = Document.objects.get(application_number=rr.applicationnumber, file_name=newfilename,reception_idno=rr.receptionid_id)
                os.remove(existing_doc.file_path)
                existing_doc.delete()
            except Document.DoesNotExist:
                pass

            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        
            Document.objects.create(
                application_number=rr.applicationnumber,
                file_path=file_path,
                file_name=newfilename,
                reception_idno=rr.receptionid_id,
                username=username,
                role=userrole,
                usersdetailsid=uid,
                platform = 'reporter'
            )

        return redirect ('/reporter/reporterhome/')
    rr=ReporterReport.objects.get(pk=repid)
    if(rr.inspectiondate != None):
        appdate=rr.inspectiondate.strftime("%Y-%m-%d")
    else:
        appdate=None
    documents = Document.objects.filter(application_number=rr.applicationnumber,reception_idno=rr.receptionid_id, platform = 'reporter')
    return render(request,'reporter/reporterform.html',{'recptreport':rr,'appdd':appdate,'documents':documents})

class Geomapview(View):
    template_name = 'reporter/geomap.html'

    def get(self, request,pk=None):
        key =settings.GOOGLE_MAPS_API_KEY
        if request.user.is_authenticated:
            useremail = request.user.email
            userid = User.objects.get(email=useremail).id
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            if userrole == "Admin":
                  eligable_locations = ReporterReport.objects.filter(placeid__isnull=False)  
                   
            else:
                  eligable_locations = ReporterReport.objects.filter(placeid__isnull=False,receptionid__reportperson=userid)
                #   completedrequest=ReporterReport.objects.filter(receptionid__reportperson=userid)
                  

        # eligable_locations = ReporterReport.objects.filter(placeid__isnull=False)
        maplocations = []

        for a in eligable_locations: 
            data = {
                'id':a.id,
                'lat': float(a.lat), 
                'lng': float(a.lng), 
                'name': a.name,
                'add1': a.add1,
                'add2': a.add2,
                'city': a.city,
                'landmark': a.landmark,
                'govrate':a.govtaprovelandrate,
                'recomrate':a.recommendedlandrate,
                
            }

            maplocations.append(data)
    # below lines are only to update in data base the lat and lng and place id 
        locations = ReporterReport.objects.values('id','add1', 'add2','city','region','country','landmark','zip','lat','lng','placeid')
        for location in locations:
            # print(location['add1'])
            if location['lat'] and location['lng'] and location['placeid'] !=None:
                lat=location['lat']
                lng=location['lng']
                placeid=location['placeid']
                label = "from database"
            elif(location['add1'] and location['city'] and location['region'] and location['country']  and location['zip'] != None):
                address_string = str(location['add1'])+','+str(location['add2'])+','+str(location['region'])+','+str(location['city'])+','+str(location['country'])+','+str(location['landmark'])+',',str(location['zip'])
                gmap =  googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
                result = gmap.geocode(address_string)[0]

                lat = result.get('geometry',{}).get('location',{}).get('lat',None)
                lng = result.get('geometry',{}).get('location',{}).get('lng',None)
                placeid = result.get('place_id',{})
                label = "from api call"
                # below commented code is just to understand how we are getting lat and lng value hirarchiely from google api
                # geometry = result.get('geometry',{})
                # placeid = result.get('place_id',{})
                # locationplace = geometry.get('location',{})
                # lat = locationplace.get('lat',None)
                # lng = locationplace.get('lng',None)
                rr=ReporterReport.objects.get(pk=location['id'])
                rr.lat =lat
                rr.lng = lng
                rr.placeid = placeid
                rr.save()

            else:
                result = ""
                lat = ""
                lng = ""
                placeid = ""
                label = "neither api nor database "
        locations = ReporterReport.objects.values('id','name','add1', 'add2','city','region','country','landmark','zip','lat','lng','placeid')
        
        context = {
                    'locations':locations,
                    'key':key,
                    'maplocations':maplocations,
                    'username':username,
                    # 'result':result,
                    # 'geometry':geometry,
                    # 'locationplace':locationplace,
                    # 'latitude':lat,
                    # 'longitude':lng,
                    # 'placeid':placeid,
                    'label':label
                   }
        
        return render(request, self.template_name, context)
