from django.shortcuts import render, redirect,get_object_or_404
from .models import ReceptionReport,Document,RecDynamicdValue
from propval.models import UserDetails, Banks,Impdoc,EngDynamicField,EngFormOptionValues,EngFormsubOptionValues
import datetime
from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect,JsonResponse,FileResponse,HttpResponse
from django.conf import settings
import os , zipfile
import io,requests,time
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from PIL import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
from django.contrib.auth.decorators import login_required
from reporter.models import ReporterReport
from django.urls import reverse 
from django.utils.text import slugify
from django.db.models import OuterRef, Subquery  


# Create your views here.

def add_report(request):
    if request.user.is_authenticated:
        useremail = request.user.email
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).id
    
    try: 
            engdynamicfields=EngDynamicField.objects.filter(active=True,form_type = "Reception form")
    except:
            engdynamicfields=[]

    if request.method == "POST":
        # print(request.POST.get('npa'))
        # print(request.POST)
        if request.POST.get('npa'):
            recnpa =True
        else:
            recnpa = False
        if request.POST.get('partcase'):
            recpartcase =True
        else:
            recpartcase = False
        app_date = request.POST.get('appdate')
        app_number = request.POST.get("appno")
        app_name = request.POST.get("name")
        app_bankname = Banks.objects.get(pk=request.POST.get("bankid")).name
        app_bankid = request.POST.get("bankid")
        app_bankvertical = request.POST.get("bankvertical")
        app_add1 = request.POST.get("add1")
        app_add2 = request.POST.get("add2")
        app_city = request.POST.get("city")
        app_region = request.POST.get("region")
        app_zip = request.POST.get("zip")
        app_country = request.POST.get("country")
        app_phonenumber = request.POST.get("phonenumber")
        app_visitor = request.POST.get("visitor")
        app_reporter = request.POST.get("reporter")
        # print(app_visitor+'A')
        if app_reporter =='' or app_reporter =='0':
            reprtr = 'Reporter Not Assigned'
        else:
            reprtr =  UserDetails.objects.get(user=app_reporter).first_name+' '+UserDetails.objects.get(user=app_reporter).last_name      
        if app_visitor =='' or app_visitor =='0':
            visitr = 'Engineer Not Assigned'
        else:
            visitr =  UserDetails.objects.get(user=app_visitor).first_name+' '+UserDetails.objects.get(user=app_visitor).last_name 

        
        rr=ReceptionReport()
        rr.applicationdate=app_date
        rr.applicationnumber=app_number
        rr.name=app_name
        rr.bankname=app_bankname
        rr.bankid=app_bankid
        rr.bankvertical=app_bankvertical
        rr.add1=app_add1
        rr.add2=app_add2
        rr.city=app_city
        rr.region=app_region
        rr.zip=app_zip
        rr.country=app_country
        rr.phonenumber=app_phonenumber
        rr.visitingperson=app_visitor
        rr.reportperson=app_reporter
        # print(app_reporter)
        rr.visitingpersonname= visitr
        rr.reportpersonname=reprtr
        rr.npa=recnpa
        rr.partcase=recpartcase
        rr.save()
        newrecid=rr.id
        floorsengid = ReceptionReport.objects.get(pk = newrecid)

        for field in engdynamicfields:  
                if(field.input_type == 'checkbox'): 
                    field_value = request.POST.getlist(field.label.replace(' ', '-').lower())
                    for fld in field_value: 
                        RecDynamicdValue.objects.create(input_field=field,value=fld,engreportid=floorsengid)
                else:
                     if(field.input_type == 'select'):
                        optionvalue = request.POST.get(field.label.replace(' ', '-').lower()) 
                        try: 
                            field_value= EngFormOptionValues.objects.get(pk=int(optionvalue)).opt_value
                        except:
                            field_value=None
                        field_valuea=None
                        if field.suboption:
                            sublabel = f'sub{field.label.replace(" ", "-").lower()}'
                            optionsubvalue = request.POST.get(sublabel) 
                            try:
                                field_valuea= EngFormsubOptionValues.objects.get(pk=int(optionsubvalue)).name
                            except:
                                field_valuea=None
                        # print(optionsubvalue, field_value)
                        # form_data[field.label] = field_value  
                        RecDynamicdValue.objects.create(input_field=field,value=field_value,subvalue=field_valuea,engreportid=floorsengid)  
                     else:
                            
                        field_value = request.POST.get(field.label.replace(' ', '-').lower()) 
                        # sublabel = f'sub{field.label.replace(" ", "-").lower()}'
                        field_valuea=None
                        # field_valuea = request.POST.get(sublabel) 
                        # print(sublabel)
                        # form_data[field.label] = field_value  
                        RecDynamicdValue.objects.create(input_field=field,value=field_value,subvalue=field_valuea,engreportid=floorsengid)

        uploaded_files = request.FILES.getlist('receptionFiles') 
        for uploaded_file in uploaded_files:
            newfilename = app_number + "_"+str(newrecid)+"_"+str(time.time())+'_' + uploaded_file.name
            file_path = os.path.join(settings.MEDIA_ROOT,'reception', newfilename)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            Document.objects.create(
                application_number=app_number,
                file_path='reception/'+newfilename,
                file_name=newfilename,
                reception_idno=newrecid,
                username=username,
                role=userrole,
                usersdetailsid=uid,
                platform = 'reception'
                
            )

        return redirect ('/reception/receptionhome/')
    ers=UserDetails.objects.filter(role='Engineer').values('user_id','id','first_name','last_name')
    # for er in ers:
    #     print(er)
    rrs=UserDetails.objects.filter(role='Reporter').values('user_id','id','first_name','last_name')
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
        # print(states[0]['state_name']) 
    #  print("Error:", response.status_code, response.json())  
    currdate=datetime.date.today().strftime("%Y-%m-%d")
    
    optvalues = EngFormOptionValues.objects.select_related('eng_dynamic_field').all()
    suboptions = EngFormsubOptionValues.objects.select_related('main_option').all()
    return render(request,"reception/receptionreport.html",{'engineers':ers,'reporters':rrs,'banks':banks,'states':states,'currdate':currdate,'engdynamicfields':engdynamicfields,'optvalues':optvalues,'suboptions':suboptions})
@login_required(login_url='login')
def receptionhome(request):
    allreports = ReceptionReport.objects.all()
    banks= Banks.objects.all().values('id','name','branch','city')
    context = {
        'api_base_url': settings.API_BASE_URL,
    }
    recpreport=ReceptionReport.objects.all().order_by('-priority','-updated_at')
    totrep=ReceptionReport.objects.all().count()
    user_details = UserDetails.objects.filter(user_email=request.user.email).first()
    if not user_details:
        return HttpResponse('User data does not exist')
        # return render (request,'home.html',{'userdata':userdetails})
    
    if user_details.role == 'Admin' or user_details.role == 'Reception':
        # return redirect('home')
        impdocs= Impdoc.objects.all()
        return render(request,"reception/receptionhome.html",{'recpreports':recpreport,'totrep':totrep,'context':context,'allreports':allreports,'impdocs':impdocs,'banks':banks})
    elif user_details.role == 'Engineer':
        return redirect('/engineer/engineerhome/')
    # elif user_details.role == 'Reception':
    #     return redirect('/reception/receptionhome/')
    elif user_details.role == 'Reporter':
        return redirect('/reporter/reporterhome/')
    # return render(request,"reception/receptionhome.html",{'recpreports':recpreport,'totrep':totrep,'context':context})

    # context = {
    #     'api_base_url': settings.API_BASE_URL,
    #     'recpreports': recpreport,
    #     'totrep': totrep,
    # }
    # return render(request, "reception/receptionhome.html", context)

def del_report(request,repid):
    # print (repid)
    rr=ReceptionReport.objects.get(pk=repid)
    if rr.engineer == 'Submitted' or rr.reporter == 'Submitted':
        totno=ReceptionReport.objects.all().count()
        return JsonResponse({'success': False,'message': 'Cannot delete record. Report is in submitted state.','total': totno})
    else:
        rr.delete()
    totno=ReceptionReport.objects.all().count()
    print(totno)
    return JsonResponse({'success': True,'message': 'Record removed successfully','total': totno})

def update_report(request,repid):
    # rr = get_object_or_404(ReceptionReport, pk=repid)
    if request.user.is_authenticated:
        useremail = request.user.email
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).id
    if request.method == "POST":
        if request.POST.get('npa'):
            recnpa =True
        else:
            recnpa = False
        if request.POST.get('partcase'):
            recpartcase =True
        else:
            recpartcase = False
        app_date = request.POST.get('appdate')
        app_number = request.POST.get("appno")
        app_name = request.POST.get("name")
        # app_bankname = request.POST.get("bankname")
        app_bankname = Banks.objects.get(pk=request.POST.get("bankid")).name
        app_bankid = request.POST.get("bankid")
        app_bankvertical = request.POST.get("bankvertical")
        app_add1 = request.POST.get("add1")
        app_add2 = request.POST.get("add2")
        app_city = request.POST.get("city")
        app_region = request.POST.get("region")
        app_zip = request.POST.get("zip")
        app_country = request.POST.get("country")
        app_phonenumber = request.POST.get("phonenumber")
        app_visitor = request.POST.get("visitor")
        app_reporter = request.POST.get("reporter")
        if app_visitor =='' or app_visitor =='0':
            engr = 'Engineer Not Assigned'
        else:
            engr =  UserDetails.objects.get(user=app_visitor).first_name+' '+UserDetails.objects.get(user=app_visitor).last_name      
        if app_reporter =='' or app_reporter =='0':
            reprtr = 'Reporter Not Assigned'
        else:
            reprtr =  UserDetails.objects.get(user=app_reporter).first_name+' '+UserDetails.objects.get(user=app_reporter).last_name      

        rr=ReceptionReport.objects.get(pk=repid)
        rr.applicationdate=app_date
        rr.applicationnumber=app_number
        rr.name=app_name
        rr.bankname=app_bankname
        rr.bankid=app_bankid
        rr.bankvertical=app_bankvertical
        rr.add1=app_add1
        rr.add2=app_add2
        rr.city=app_city
        rr.region=app_region
        rr.zip=app_zip
        rr.country=app_country
        rr.phonenumber=app_phonenumber
        rr.visitingperson=app_visitor
        rr.reportperson=app_reporter
        # rr.visitingpersonname= UserDetails.objects.get(user=app_visitor).first_name+' '+UserDetails.objects.get(user=app_visitor).last_name 
        rr.visitingpersonname= engr
        rr.reportpersonname=reprtr
        rr.npa = recnpa
        rr.partcase = recpartcase
        # print(app_visitor,app_reporter,'B')
        rr.save()

        RecDynamicdValue.objects.filter(engreportid=repid).delete()
        floorsengid = ReceptionReport.objects.get(pk = repid)
        # saving dynamic fields details
        try: 
            engdynamicfields=EngDynamicField.objects.filter(active=True,form_type="Reception form")
        except:
            engdynamicfields=[]
        for field in engdynamicfields:  
        # Get the submitted value from request.POST 
            if(field.input_type == 'checkbox'): 
                field_value = request.POST.getlist(field.label.replace(' ', '-').lower())
                for fld in field_value: 
                    RecDynamicdValue.objects.create(input_field=field,value=fld,engreportid=floorsengid)
            else: 
                if(field.input_type == 'select'):
                    optionvalue = request.POST.get(field.label.replace(' ', '-').lower()) 
                    try: 
                        field_value= EngFormOptionValues.objects.get(pk=int(optionvalue)).opt_value
                    except:
                        field_value=None
                    field_valuea=None
                    if field.suboption:
                        sublabel = f'sub{field.label.replace(" ", "-").lower()}'
                        optionsubvalue = request.POST.get(sublabel)
                        print(sublabel)
                        try: 
                            field_valuea= EngFormsubOptionValues.objects.get(pk=int(optionsubvalue)).name
                        except:
                            field_valuea=None
                    RecDynamicdValue.objects.create(input_field=field,value=field_value,subvalue=field_valuea,engreportid=floorsengid)  
                else:
                        
                    field_value = request.POST.get(field.label.replace(' ', '-').lower()) 
                    field_valuea=None
                    if field_value:
                        RecDynamicdValue.objects.create(input_field=field,value=field_value,subvalue=field_valuea,engreportid=floorsengid)

        uploaded_files = request.FILES.getlist('receptionFiles')
        for uploaded_file in uploaded_files:
            newfilename = f"{app_number}_{str(repid)}_{str(time.time())}_{uploaded_file.name}"
            file_path = os.path.join(settings.MEDIA_ROOT,'reception', newfilename)

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
                file_path='reception/'+newfilename,
                file_name=newfilename,
                reception_idno=repid,
                username=username,
                role=userrole,
                usersdetailsid=uid,
                platform = 'reception'
            )

        return redirect ('/reception/receptionhome/')
    rr=ReceptionReport.objects.get(pk=repid)
    appdate=rr.applicationdate.strftime("%Y-%m-%d")
    ers=UserDetails.objects.filter(role='Engineer').values('id','user_id','first_name','last_name')
    rrs=UserDetails.objects.filter(role='Reporter').values('id','user_id','first_name','last_name')
    documents = Document.objects.filter(application_number=rr.applicationnumber,reception_idno=repid, platform = 'reception')
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
    
    subquery = RecDynamicdValue.objects.filter(
            engreportid=repid,
            input_field_id=OuterRef('input_field_id')
            ).order_by('id').values('id')[:1]
    engdynamicvalues = RecDynamicdValue.objects.filter(id__in=Subquery(subquery))
    engdynamiccheckvalues = list(RecDynamicdValue.objects.values_list('value', flat=True).filter(engreportid=repid))    
    optvalues = EngFormOptionValues.objects.select_related('eng_dynamic_field').all()
    suboptions = EngFormsubOptionValues.objects.select_related('main_option').all()
    
    return render(request,'reception/receptionreport.html',{'recptreport':rr,'appdd':appdate,'engineers':ers,'reporters':rrs,'documents':documents,'banks':banks,'states':states,'engdynamicvalues':engdynamicvalues,'optvalues':optvalues,'engdynamiccheckvalues':engdynamiccheckvalues,'suboptions':suboptions})

def delete_file(request, doc_id):
    try:
        document = Document.objects.get(pk=doc_id)
        os.remove(os.path.join(settings.MEDIA_ROOT,document.file_path))
        document.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Document.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Document does not exist'})
    
def engcompreportpdf(request, doc_id):
    api_base_url= settings.API_BASE_URL
    # url=api_base_url+'engineer/'+str(doc_id)
    url = f'{api_base_url}engineer/{doc_id}/engcomjobpdfarctoo' 
    # print(str(doc_id), url)
    width, height = letter
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data1 = response.json()
        data = data1['data'][0]
        print(data['receptionid'])
        # print(data['data'][0]['updated_at'])
        # return JsonResponse(data)
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=500)
    except Exception as err:
        return JsonResponse({'error': f'Other error occurred: {err}'}, status=500)
    date_str = data["updated_at"]
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    buf = io.BytesIO()
    c= canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textobj=c.beginText(40,680)
    textobj.setTextOrigin(60,72)  # instead inch inch use 72 to 1 inch margin
    textobj.setFont("Helvetica",14)
    textobj.setFillColor(colors.black)

    

    # Define your styles
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleN.alignment = TA_LEFT
    styleN.fontSize = 14
    # styleN.leading = 16

    textobja=c.beginText(40,680)
    textobja.setTextOrigin(300,72)  # instead inch inch use 72 to 1 inch margin
    textobja.setFont("Helvetica",14)
    textobja.setFillColor(colors.black)
    linesa=[f'<b>Completion Date:</b> {date_obj.strftime("%d-%m-%Y")}',f'',f'<b>Visit done in presence of:</b> {data["visitinpresence"]}',f'',
             f'<b>Case Type:</b> {data["casetype"]}',]
    for linea in linesa:
        p = Paragraph(linea, styleN)
        p.wrapOn(c, 500, 100)  # Adjust width and height as needed
        p.drawOn(c, textobja.getX(), textobja.getY())
        textobja.moveCursor(0, 14)
        # width, height = p.wrap(1000, 500)  # Adjust width and height as needed
        # p.drawOn(c, textobja.getX(), textobja.getY() - height)
        # textobja.moveCursor(0, height)  # Move cursor down for the next line
        c.drawText(textobja)
        # textobja.textLine(linea)

    textobjb=c.beginText(40,680)
    textobjb.setTextOrigin(300,270)  # instead inch inch use 72 to 1 inch margin
    textobjb.setFont("Helvetica",14)
    textobjb.setFillColor(colors.black)
    linesb=[f'<b>West:</b> {data["west"]}',f'<b>South:</b> {data["south"]}',]
    for lineb in linesb:
        p = Paragraph(lineb, styleN)
        p.wrapOn(c, 500, 100)  # Adjust width and height as needed
        p.drawOn(c, textobjb.getX(), textobjb.getY())
        textobjb.moveCursor(0, 14)
        c.drawText(textobjb)
        # textobjb.textLine(lineb)


    lines =[
        f'<b>Application Number:</b> {data["applicationnumber"]}',
        f'',
        f'<b>Customer Name:</b> {data["name"]}',
        f'',
        f'<b>Bank Name:</b> {data["bankname"]}',
        f'',
        "<b>Address:</b>",f'',
        f'{data["add1"]}{" ,"}',
        f'{data["add2"]}{" ,"}',
        f'{data["city"]}{", "}{data["region"]}{", "}{data["zip"]}{", "}{data["country"]}',
        f'',
        "<b>Boundaries as per site:</b>",f'',
        f'<b>East:</b> {data["east"]}',
        f'<b>North:</b> {data["north"]}',
        f'',
        "<b>Floor details(Area Sq.ft.):</b>",f'',
        f'<b>Ground floor :</b> {data["gfarea"]}{"   " * 40}<b>First floor:</b> {data["ffarea"]}{"   " * 20}<b>Second floor:</b> {data["sfarea"]}{"   " * 20}<b>Third floor:</b> {data["tfarea"]}',
        f'',
        f'<b>Age of the property:</b> {data["propertyage"]}{" " * 10}<b>Land Rate:</b> {data["landrate"]}{" " * 10}<b>Occupant:</b> {data["Occupant"]}',
        f'',
        f'<b>Land Mark:</b> {data["landmark"]}{" " * 10}<b>Rented:</b> {data["rented"]}{" " * 10}<b>Road width:</b> {data["roadwidth"]}','',
        "<b>Hazards:</b>",

    ]
    pdffilename=data["name"]+'_'+str(doc_id)+'_'+data["applicationnumber"]+'.pdf'
    for line in lines:
        p = Paragraph(line, styleN)
        p.wrapOn(c, 500, 100)  # Adjust width and height as needed
        p.drawOn(c, textobj.getX(), textobj.getY())
        textobj.moveCursor(0, 14)
        c.drawText(textobj)
        # textobj.textLine(line)
        
    width, height = letter
    checkbox_x = 70  
    checkbox_y = height - 345 
    if (data["hightensionline"]):
        c.rect(checkbox_x, checkbox_y, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+10,"High Tension Line")
    if (data["railwayline"]):
        c.rect(checkbox_x, checkbox_y+20, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+20, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+30,"Railway Line")
    if (data["nala"]):
        c.rect(checkbox_x, checkbox_y+40, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+40, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+50,"Nala")
    if (data["river"]):
        c.rect(checkbox_x, checkbox_y+60, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+60, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+70,"River")
    if (data["pahad"]):
        c.rect(checkbox_x, checkbox_y+80, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+80, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+90,"pahad")
    if (data["roadcomesunderroadbinding"]):
        c.rect(checkbox_x, checkbox_y+100, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+100, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+110,"Road comes under Road Binding")
    if (data["propertyaccessissue"]):
        c.rect(checkbox_x, checkbox_y+120, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+120, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+130,"Property Access issue")
    if (data["othercheck"]):
        c.rect(checkbox_x, checkbox_y+140, 10, 10, stroke=1, fill=1)  
    else:
        c.rect(checkbox_x, checkbox_y+140, 10, 10, stroke=1, fill=0) 
    c.drawString(checkbox_x+20, checkbox_y+150,"Other please specify")
    if (data['others']):
        c.drawString(checkbox_x+20, checkbox_y+170,data['others'])
    c.drawString(checkbox_x, checkbox_y+190,"Remark :   ")
    if (data['remark']):
        c.drawString(checkbox_x+60, checkbox_y+190,data['remark'])
    # c.drawString(0,10,"A")
    # c.drawString(300,10,"B")
    # c.drawString(600,10,"C")
    c.setFillColorRGB(0,0,255)
    c.setFont("Courier-Bold",16)
    c.setTitle(pdffilename)
    c.line(10,40,600,40)
    img = Image.open('propval/static/img/logo.png')
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Adjust as needed
    rgb_img = img.convert('RGB')
    rgb_img.save('llogo.jpg')
    c.drawInlineImage('llogo.jpg',20,-20,25,25)
    if (data['receptionid']['visitingpersonname']):
        c.drawCentredString(330,30, f"Site Visit Report submitted by: {data['receptionid']['visitingpersonname']} ")
    c.drawText(textobj)
    c.drawText(textobja)
    c.drawText(textobjb)
    c.showPage()
    documents = Document.objects.filter(application_number=data["applicationnumber"],reception_idno=data['receptionid']['id'], platform = 'engineer')
    # print (data["applicationnumber"],data['receptionid']['id'],documents)
    i=1
    y=0
    icon_x = 550
    icon_y = 5  # Adjust y-coordinate to position the icon correctly
    icon_width = 50
    icon_height = 50
    icon_y_click = height-55
    # Draw a rectangle where you would like the download icon to be  
    c.drawImage('propval/static/img/download.png', icon_x, icon_y, width=icon_width, height=icon_height)  

    # Set link for the icon (assuming you have a download view)  
    file_ids = ','.join(str(id) for id in documents.values_list('id', flat=True))
    # file_ids = '1,2,3'
    download_url = request.build_absolute_uri(reverse('download_image', args=[file_ids]))  #download_image is view to download image
    print(download_url)
    # c.linkURL(download_url, (550, 50, 50, 800), relative=1)  
    c.linkURL(download_url, (icon_x, icon_y_click, icon_x + icon_width, icon_y_click + icon_height), relative=1)  
        # like this  path('download-image/', download_image, name='download_image'),  
    for doc in documents:
        
        # print (doc.file_name)
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')  
        if(doc.file_name.lower().endswith(valid_extensions)):  
            img = Image.open(os.path.join(settings.MEDIA_ROOT,doc.file_path))
            img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Adjust as needed
            rgb_img = img.convert('RGB')
            rgb_img.save(doc.file_name)
            c.drawImage(doc.file_name,20,y,250,250)
            
            if(i==2):
                c.showPage()
                i=0
                y=-300
        i=i+1
        y=y+300
    c.save()
    buf.seek(0)

    # Get the query parameter to decide on viewing or downloading  
    download = request.GET.get('download', 'false')  # Default to downloading  

    if download.lower() == 'false':  
        # Set headers for viewing inline  
        response = FileResponse(buf, as_attachment=False, filename=pdffilename)  
        response['Content-Disposition'] = f'inline; filename={pdffilename}'  
    else:  
        # Set headers for downloading  
        response = FileResponse(buf, as_attachment=True, filename=pdffilename)  

    return response 

    # return FileResponse(buf,as_attachment=True,filename='engreport')
def repcompreportpdf(request, doc_id):
    data = ReporterReport.objects.get(pk=doc_id)
    appdate=data.inspectiondate.strftime("%d-%m-%Y")
    documents = Document.objects.filter(application_number=data.applicationnumber,reception_idno=data.receptionid.id,platform='reporter')
    # print(data.receptionid.id)
    # for document in documents:
    #     print(document.file_name, document.file_path)
    return render(request,'reporter/reporterreport.html',{"requestreceived":data,"appdd":appdate,"documents":documents,"MEDIA_URL":settings.MEDIA_URL})
def download_image(request,file_ids):

    # Split the incoming file_ids (from URL) into a list  
    ids = file_ids.split(',')  
    
    # Prepare a ZIP file  
    zip_filename = 'downloaded_files.zip'  
    zip_filepath = os.path.join('media', zip_filename)  # Adjust path as needed  
    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:  
        for file_id in ids:  
            file_instance = get_object_or_404(Document, id=file_id)  
            file_path = os.path.join(settings.MEDIA_ROOT,file_instance.file_path )   
            zip_file.write(file_path, os.path.basename(file_path))  # Add file to the zip  

    # Create a response with the ZIP file  
    response = HttpResponse(content_type='application/zip')  
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'  
    
    # Open the ZIP file in binary read mode and write to the response  
    with open(zip_filepath, 'rb') as zip_file:  
        response.write(zip_file.read())  
    # Optionally, you can delete the zip file after downloading  
    os.remove(zip_filepath)  
    
    return response  
    # below code is for one file download
    # file_instance = get_object_or_404(Document, id=file_id)   
    # file_path = os.path.join(settings.MEDIA_ROOT,file_instance.file_path )  
    # response = HttpResponse(open(file_path, 'rb'), content_type='application/octet-stream')  
    # response['Content-Disposition'] = f'attachment; filename="{file_instance.file_name}"'  
    # return response  

