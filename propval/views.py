from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import datetime, os,requests
from django.http import JsonResponse
from reception.models import ReceptionReport,ArchieveReceptionReport
from reporter.models import ReporterReport
from .models import UserDetails, CompanyProfile,Banks
from django.db.models import Count
from django.views.decorators.http import require_POST
import sqlite3
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views import View
from django.db.models import OuterRef, Subquery
from rest_framework import viewsets  
from .models import UserActivity  
from .serializers import UserActivitySerializer


# Create your views here.
#from django.views.decorators.csrf import ensure_csrf_cookie

#@ensure_csrf_cookie
@login_required(login_url='login')
def Home(request):
    userno=[]
    userno1=[]
    role_order = ['Admin', 'Reception', 'Engineer', 'Reporter']
    role_counts = UserDetails.objects.values('role').annotate(user_count=Count('id'))
    role_count_dict = {role: 0 for role in role_order}
    for entry in role_counts:
        role = entry['role']
        if role in role_order:
            userno.append(entry['user_count'])
            role_count_dict[role] = entry['user_count']
            
            # userno.append(entry['user_count'])
    print(role_count_dict)
    # userno1=role_count_dict['Admin'],role_count_dict['Reception'],role_count_dict['Engineer'],role_count_dict['Reporter']
    ['userno1'].append(role_count_dict['Admin'])
    # ,role_count_dict['Reception'],role_count_dict['Engineer'],role_count_dict['Reporter']
    # for rlcd in role_count_dict :
    #     userno.append(entry['user_count'])
    # print(userno1)
    dictusersno={
      "usersno":[]
    }
    # for rl in role_count_dict:
    dictusersno["usersno"].append(role_count_dict['Admin'])
    dictusersno["usersno"].append(role_count_dict['Reception']) 
    dictusersno["usersno"].append(role_count_dict['Engineer']) 
    dictusersno["usersno"].append(role_count_dict['Reporter']) 

    userdetails = UserDetails.objects.select_related('user').exclude(user__last_name='deleted') 

    user_details = UserDetails.objects.filter(user_email=request.user.email).first()

    context = {
        'api_base_url': settings.API_BASE_URL,
    }
    recpreport=ReceptionReport.objects.all().order_by('-priority','updated_at')
    totrep=ReceptionReport.objects.all().count()
    
    if not user_details:
        # return HttpResponse('User data does not exist')
        return render (request,'home.html',{'userdata':userdetails})
    
    if user_details.role == 'Admin':
        # return redirect('home')
        # reporterwisecomp = ReceptionReport.objects.filter(reporter='Submitted').values('reportperson').annotate(count=Count('reportperson'))
        # reporterwisetot = ReceptionReport.objects.values('reportperson','reporter').annotate(count=Count('reportperson'))
       
        # queryset = ReceptionReport.objects.values('reportperson','reportpersonname').annotate(
        # submitted_count=Count(Case(
        #     When(reporter='Submitted', then=1),
        #     output_field=IntegerField(),
        #     )),
        #     other_count=Count(
        #         Case(When(~Q(reporter='Submitted1'), then=1),
        #         output_field=IntegerField(),
        #     ))
        # ).order_by('reportperson')
        # queryset = ReporterReport.objects.select_related('userdetailsid__userdetails').filter(receptionid__reporter='Submitted')  
        # queryset = ReporterReport.objects.select_related('userdetailsid__userdetails').values(
        #     'receptionid__reportperson','receptionid__reportpersonname','userdetailsid__userdetails__profileimage').annotate(
        # submitted_count=Count(Case(
        #     When(receptionid__reporter='Submitted', then=1),
        #     output_field=IntegerField(),
        #     )),
        #     other_count=Count(
        #         Case(When(~Q(receptionid__reporter='Rubmitted1'), then=1),
        #         output_field=IntegerField(),
        #     )),
        # ).order_by('receptionid__reportperson')
        reporter_count_subquery = ReceptionReport.objects.filter(reportperson=OuterRef('receptionid__reportperson'))\
        .values('reportperson')\
        .annotate(reporter_count=Count('reportperson'))\
        .values('reporter_count') 
        queryset = ReporterReport.objects.select_related('userdetailsid__userdetails').values(
            'receptionid__reportperson','receptionid__reportpersonname','userdetailsid__userdetails__profileimage'
            ,'userdetailsid__userdetails__first_name','userdetailsid__userdetails__last_name').annotate(
            submitted_count=Count('userdetailsid_id'), 
            other_count=Subquery(reporter_count_subquery)  # Total count of visitingperson using subquery     
        ).order_by('receptionid__reportperson')
        # working_records = ReceptionReport.objects.prefetch_related('engineerreport_set','reporterreport_set').all()  
        # archive_records = ArchieveReceptionReport.objects.prefetch_related('engineerreport_set','reporterreport_set').all()  
         
# Combine the querysets using union  
        # allreports = working_records.union(archive_records)  
        # for report in allreports:
        #     print(report.id)
        #     try:
        #         engId=report.engineerreport_set.get(receptionid_id=report.id)
        #     except :
        #         engId=None
        #     if engId is not None:
        #         print(engId.id,engId.name)
        #     print(engId)
        allreports = ReceptionReport.objects.all()
        return render (request,'home.html',{'userdata':userdetails,'usno':dictusersno,'recpreports':recpreport,'totrep':totrep,'context':context,'repwise':queryset,'allreports':allreports})
    elif user_details.role == 'Engineer':
        return redirect('/engineer/engineerhome/')
    elif user_details.role == 'Reception':
        return redirect('/reception/receptionhome/')
    elif user_details.role == 'Reporter':
        return redirect('/reporter/reporterhome/')

    
    return render (request,'home.html',{'userdata':userdetails})
    
def Signup(request):
    if request.method=='POST':
        ufname = request.POST.get('firstname')
        ulname = request.POST.get('lastname')
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        uconfpassword = request.POST.get('confpassword')
        role = request.POST.get('role')
        if upassword!=uconfpassword:
        #    return HttpResponse('Password and confirm password does not match')
            messages.success(request, "Password and confirm password does not match!")  
            return redirect('signup')  
        #    return JsonResponse({'error': 'confpassword','message': 'Password and confirm password does not match'})
        #else:
        try:  
            user = User.objects.get(username=uemail)  
            # return HttpResponse('User or email already exists') 
            # return JsonResponse({'error': 'userexists','message': 'User or email already exists'})
            messages.success(request, "User or email already exists!")  
            return redirect('signup')  
        except User.DoesNotExist:  
            my_user = User.objects.create_user(uemail,uemail,upassword)
            my_user.save()
            UserDetails.objects.create(user=my_user,first_name=ufname,last_name=ulname,role=role)
       # return HttpResponse('User has been created')
            return redirect('home')
        # return redirect('login')
        # print(uemail,upassword,uconfpassword)
    return render (request,'signup.html')

def Signin(request):

     if request.method=='POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uemail,password=upassword)
        print(user)
        if user is not None:
           login(request , user)
           return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'user name or password is not correct'})
            # return HttpResponse('user name or password is not correct')   
        
     return render (request,'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def changepassword(request):
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user, data=request.POST) 
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)  # Important! Update the session with the new password.
            messages.success(request,"Your password has been changed successfully!")
            return redirect('login')
    else:   
        fm=PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'fm':fm})

    
def profile(request, uid=0):
    if(uid == 0):
        userdetails = UserDetails.objects.filter(user_email=request.user.email).first()
    else:
        userdetails = UserDetails.objects.get(pk=uid)
    # print(settings.MEDIA_ROOT)
    if not userdetails:
        return HttpResponse('User data does not exist')
    if request.method == 'POST':
        print(userdetails.first_name , userdetails.last_name)
        userdetails.first_name = request.POST.get('first_name')
        userdetails.last_name = request.POST.get('last_name')
        userdetails.user_email = request.POST.get('email')
        userdetails.phone = request.POST.get('phone')
        userdetails.add1 = request.POST.get('add1')
        userdetails.add2 = request.POST.get('add2')
        userdetails.city = request.POST.get('city')
        userdetails.region = request.POST.get('region')
        userdetails.zip = request.POST.get('zip')
        userdetails.country = request.POST.get('country')
        userdetails.bankname = request.POST.get('bankname')
        userdetails.bankacno = request.POST.get('acno')
        userdetails.ifsccode = request.POST.get('ifsc')
        uploaded_files = request.FILES.getlist('profileimage') 
        # uploaded_files = request.FILES.['profileimage'] 
        profile_dir = os.path.join(settings.MEDIA_ROOT, 'profile')  
        os.makedirs(profile_dir, exist_ok=True)
        if uploaded_files:    
            for uploaded_file in uploaded_files:
                newfilename = userdetails.first_name+'_'+str(userdetails.user_id)+'_'+uploaded_file.name
                # print(newfilename, request.POST.get('first_name'))
                file_path = os.path.join(settings.MEDIA_ROOT,'profile', newfilename)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            userdetails.profileimage = 'profile/'+newfilename
        userdetails.save()
        if(uid == 0):
            next_url = request.GET.get('next', '/default-url/')
            return redirect(next_url) 
        else:
            return redirect('home')
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
    if response.status_code == 200:  
        allstates = response.json()  
        states=allstates.get('states')
    else:  
        states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
    return render (request,'profile.html',{'userdata':userdetails,'uid':uid,'states':states})


# @require_POST
def del_user(request,uid,udid):
    print (uid,udid)
    u=User.objects.get(pk=uid)
    u.last_name='deleted'
    u.save()
    # u.delete()
    # ud=UserDetails.objects.get(pk=udid)
    # ud.delete()
    return JsonResponse({'success': True,'message': 'User removed successfully'})
    # return redirect('home')

# @require_POST
def activateuser(request,uid):
    try:
        u=User.objects.get(pk=uid)
        if u.is_active:
            u.is_active=False
        else:
            u.is_active=True
        u.save()
        return JsonResponse({'success': True,'message': 'User Status has been changed successfully'})
    except User.DoesNotExist:
        # return redirect('home')
        return JsonResponse({'success': False, 'error':'User not found'}) 

def company_profile_view(request):
    profile = CompanyProfile.objects.first()
    
    if request.method == 'POST':
        if (profile ==None):
            profile = CompanyProfile()
        profile.name = request.POST.get('name')
        profile.address = request.POST.get('add1')+' '+request.POST.get('add2')
        profile.city = request.POST.get('city')
        profile.state = request.POST.get('region')
        profile.zip = request.POST.get('zip')
        profile.country = request.POST.get('country')
        profile.contact_no = request.POST.get('phonenumber')
        profile.std = request.POST.get('std')
        profile.phone = request.POST.get('landline')
        profile.email = request.POST.get('email')
        profile.website = request.POST.get('website')
        profile.gstin = request.POST.get('gstin')
        profile.pan = request.POST.get('pan')
        profile.bankname = request.POST.get('bankname')
        profile.bankacno = request.POST.get('bankacno')
        profile.ifsc = request.POST.get('ifsc')
        profile.terms = request.POST.get('terms')
        uploaded_files = request.FILES.getlist('companyprofilefile') 
        # Create the profile directory if it does not exist  
        profile_dir = os.path.join(settings.MEDIA_ROOT, 'profile')  
        os.makedirs(profile_dir, exist_ok=True)
        if uploaded_files:    
            for uploaded_file in uploaded_files:
                newfilename = profile.name+str(profile.id)+'_'+uploaded_file.name
                
                file_path = os.path.join(settings.MEDIA_ROOT,'profile', newfilename)
                    
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            profile.profileimage = 'profile/'+newfilename
        profile.save()
        # return redirect('companyprofile')
        next_url = request.GET.get('next', '/default-url/')
        return redirect(next_url)
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
    if response.status_code == 200:  
        allstates = response.json()  
        states=allstates.get('states')
    else:  
        states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}] 
    return render(request, 'company_profile.html', {'profile': profile, 'states': states})

def banks(request,uid=None):
    if uid !=0:
        bank = Banks.objects.get(pk=uid)
    else :
        bank=None
    
    if request.method == 'POST':
        if (bank ==None):
            bank = Banks()
        bank.name = request.POST.get('name')
        bank.branch = request.POST.get('branch')
        
        bank.add1 = request.POST.get('add1')
        bank.add2 = request.POST.get('add2')
        
        bank.city = request.POST.get('city')
        
        bank.state = request.POST.get('region')
        
        bank.zip = request.POST.get('zip')
        
        bank.country = request.POST.get('country')
        
        bank.contact_no = request.POST.get('phonenumber')
        bank.std = request.POST.get('std')
        bank.landline = request.POST.get('landline')
        
        bank.email = request.POST.get('email')
        
        bank.website = request.POST.get('website')
        
        bank.gstin = request.POST.get('gstin')
        bank.internalrate = request.POST.get('internalrate')
        bank.externalrate = request.POST.get('externalrate')
        bank.partamount = request.POST.get('partamount')
        # uploaded_files = request.FILES.getlist('companyprofilefile') 
        # if uploaded_files:    
        #     for uploaded_file in uploaded_files:
        #         newfilename = profile.name+str(profile.id)+'_'+uploaded_file.name
                
        #         file_path = os.path.join(settings.MEDIA_PROFILE, newfilename)
                    
        #         with open(file_path, 'wb+') as destination:
        #             for chunk in uploaded_file.chunks():
        #                 destination.write(chunk)
        #     profile.profileimage = file_path
        bank.save()
        # return redirect('companyprofile')
        # next_url = request.GET.get('next', '/default-url/')
        return redirect('bankmanage') 
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
    if response.status_code == 200:  
        allstates = response.json()  
        states=allstates.get('states')
    else:  
        states=[{'state_name':'Madhya Pradesh','state_id':20}, {'state_name':'Uttar Pradesh'}, {'state_name':'Rajsthan'}, {'state_name':'Delhi'}]
    return render(request, 'banks.html', {'bank': bank,'states': states})

def bankmanage(request):
    banks = Banks.objects.all()
    return render(request, 'bankmanagement.html', {'banks': banks})

def generatebill(request):
    # bills=ReceptionReport.objects.filter(reporter='Submitted')
    bills=ReporterReport.objects.all()
    banks=Banks.objects.all()
    # appdate=bills.applicationdate.strftime("%Y-%m-%d")
    return render(request, 'bills/generatebill.html', {'bills': bills,'banks': banks})
def bill(request, uid):
    # bills=ReceptionReport.objects.filter(reporter='Submitted')
    bills=ReporterReport.objects.filter(pk=uid)
    print(bills)
    # print(ReporterReport.objects.get(pk=uid).bankid_id)
    banks=Banks.objects.get(pk=ReporterReport.objects.get(pk=uid).bankid_id)
    company = CompanyProfile.objects.first()
    # appdate=bills.applicationdate.strftime("%Y-%m-%d")
    return render(request, 'bills/bill.html',{'bills': bills,'banks': banks,'company':company})
def bills(request,uid=None):
    print(uid)
    # bills=ReceptionReport.objects.filter(reporter='Submitted')
    bills=ReporterReport.objects.filter(bankid=uid)
    banks=Banks.objects.get(pk=uid)
    company = CompanyProfile.objects.first()
    # print(company.name)
    # appdate=bills.applicationdate.strftime("%Y-%m-%d")
    return render(request, 'bills/bill.html',{'bills': bills,'banks': banks,'company':company})

# def render_to_pdf(template_src, context_dict={}):
def render_to_pdf(template_src, params):
	template = get_template(template_src)
	html  = template.render(params)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class billinpdf(View):
	def get(self, request, *args, **kwargs):
            data=ReceptionReport.objects.filter(reporter='Submitted')
            bills=list(data)
            data_dict = {'items': bills}
            itemss =data_dict.get('items')
            params = {
                'today': datetime.date.today(),
                'bills':data
            }
            # print(params.get('bills')['items'][0]['name'])
            # print(data_dict.get('items')[0]['name'])
            # print(bills)
            # return
            pdf = render_to_pdf('bills/bill.html', params)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response

# user logging api

class UserActivityViewSet(viewsets.ModelViewSet):  
    queryset = UserActivity.objects.all()  
    serializer_class = UserActivitySerializer

def Userlog(request):
    useractivities = UserActivity.objects.all().order_by('-timestamp')
    return render(request, 'userlog.html', {'useractivities': useractivities})

def Archive(request):
    archives = ArchieveReceptionReport.objects.all()
    return render(request, 'archive.html', {'archives': archives})

# def update_employee(id, userdetailsid):
#     conn = sqlite3.connect('db.sqlite3')
#     cursor = conn.cursor()
#     cursor.execute("""
#         UPDATE site_engineer_engineerreport
#         SET userdetailsid = ?
#         WHERE userdetailsid = ?
#     """, (userdetailsid, id))
#     conn.commit()
#     conn.close()

# update_employee(0, 10)