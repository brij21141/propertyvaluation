from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import ReceptionReport,Document
from propval.models import UserDetails, Banks
from datetime import datetime
from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect,JsonResponse,FileResponse
from django.conf import settings
import os 
import io,requests
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

# Create your views here.

def add_report(request):
    if request.user.is_authenticated:
        useremail = request.user.email
        if(UserDetails.objects.filter(user_email=useremail).exists()):
            username = UserDetails.objects.get(user_email=useremail).first_name+" "+UserDetails.objects.get(user_email=useremail).last_name
            userrole = UserDetails.objects.get(user_email=useremail).role
            uid = UserDetails.objects.get(user_email=useremail).id
    if request.method == "POST":
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

        # # Check if application number already exists
        # if ReceptionReport.objects.filter(applicationnumber=app_number).exists():
        #     messages.error(request, "Application number already exists.")
        #     return render(request, "reception/receptionreport.html", {
        #         'recptreport': {
        #             'applicationnumber': app_number,
        #             'applicationdate': app_date,
        #             'name': app_name,
        #             'bankname': app_bankname,
        #             'bankvertical': app_bankvertical,
        #             'add1': app_add1,
        #             'add2': app_add2,
        #             'city': app_city,
        #             'region': app_region,
        #             'zip': app_zip,
        #             'country': app_country,
        #             'phonenumber': app_phonenumber,
        #             'visitingperson': app_visitor,
        #             'reportperson': app_reporter,
        #         }
        #     })

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
        rr.visitingpersonname= UserDetails.objects.get(user=app_visitor).first_name+' '+UserDetails.objects.get(user=app_visitor).last_name 
        rr.reportpersonname=reprtr
        rr.save()
        newrecid=rr.id
        uploaded_files = request.FILES.getlist('receptionFiles') 
        for uploaded_file in uploaded_files:
            newfilename = app_number + "_"+str(newrecid)+"_" + uploaded_file.name
            file_path = os.path.join(settings.MEDIA_ROOTRECEPTION, newfilename)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            Document.objects.create(
                application_number=app_number,
                file_path=file_path,
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
    return render(request,"reception/receptionreport.html",{'engineers':ers,'reporters':rrs,'banks':banks})
@login_required(login_url='login')
def receptionhome(request):
    allreports = ReceptionReport.objects.all()
    context = {
        'api_base_url': settings.API_BASE_URL,
    }
    recpreport=ReceptionReport.objects.all().order_by('-priority','updated_at')
    totrep=ReceptionReport.objects.all().count()
    user_details = UserDetails.objects.filter(user_email=request.user.email).first()
    if not user_details:
        return HttpResponse('User data does not exist')
        # return render (request,'home.html',{'userdata':userdetails})
    
    if user_details.role == 'Admin' or user_details.role == 'Reception':
        # return redirect('home')
        return render(request,"reception/receptionhome.html",{'recpreports':recpreport,'totrep':totrep,'context':context,'allreports':allreports})
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
        rr.visitingpersonname= UserDetails.objects.get(user=app_visitor).first_name+' '+UserDetails.objects.get(user=app_visitor).last_name 
        rr.reportpersonname=reprtr
        # print(app_visitor,app_reporter,'B')
        rr.save()

        uploaded_files = request.FILES.getlist('receptionFiles')
        for uploaded_file in uploaded_files:
            newfilename = f"{app_number}_{str(repid)}_{uploaded_file.name}"
            file_path = os.path.join(settings.MEDIA_ROOTRECEPTION, newfilename)

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
                file_path=file_path,
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
    return render(request,'reception/receptionreport.html',{'recptreport':rr,'appdd':appdate,'engineers':ers,'reporters':rrs,'documents':documents,'banks':banks})

def delete_file(request, doc_id):
    try:
        document = Document.objects.get(pk=doc_id)
        os.remove(document.file_path)
        document.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except Document.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Document does not exist'})
    
def engcompreportpdf(request, doc_id):
    api_base_url= settings.API_BASE_URL
    # url=api_base_url+'engineer/'+str(doc_id)
    url = f'{api_base_url}engineer/{doc_id}' 
    print(str(doc_id), url)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # return JsonResponse(data)
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=500)
    except Exception as err:
        return JsonResponse({'error': f'Other error occurred: {err}'}, status=500)
    date_str = data["updated_at"]
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    
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
    c.drawString(checkbox_x+20, checkbox_y+170,data['others'])
    c.drawString(checkbox_x, checkbox_y+190,"Remark :   ")
    c.drawString(checkbox_x+60, checkbox_y+190,data['remark'])
    # c.drawString(0,10,"A")
    # c.drawString(300,10,"B")
    # c.drawString(600,10,"C")
    c.setFillColorRGB(0,0,255)
    c.setFont("Courier-Bold",20)
    c.setTitle(pdffilename)
    c.line(10,40,600,40)
    img = Image.open('propval/static/img/logo.png')
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Adjust as needed
    rgb_img = img.convert('RGB')
    rgb_img.save('llogo.jpg')
    c.drawInlineImage('llogo.jpg',20,-20,25,25)
    c.drawCentredString(330,30, f"Site Visit Report submitted by: {data['receptionid']['visitingpersonname']} ")
    c.drawText(textobj)
    c.drawText(textobja)
    c.drawText(textobjb)
    c.showPage()
    documents = Document.objects.filter(application_number=data["applicationnumber"],reception_idno=data['receptionid']['id'], platform = 'engineer')
    # print (data["applicationnumber"],data['receptionid']['id'],documents)
    i=1
    y=0
    for doc in documents:
        
        # print (doc.file_name)
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')  
        if(doc.file_name.lower().endswith(valid_extensions)):  
            img = Image.open(doc.file_path)
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


