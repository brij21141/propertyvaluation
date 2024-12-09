# keep track of the user activity logged the details
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from .models import UserActivity,UserDetails
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist  



@receiver(user_logged_in)
def log_user_login(sender, user, request, **kwargs):
    # print('User {} logged in through page {}'.format(user.username,request.META.get('HTTP_REFERER')) )
    ip_address = request.META.get('REMOTE_ADDR')  
    userdetail =UserDetails.objects.get(user_id=user.id)
    UserActivity.objects.create(user=user,userdetails=userdetail, action_type='login', ip_address=ip_address)  
@receiver(user_login_failed)
def log_user_login_failed(sender, request,credentials, **kwargs):
    # print(credentials)
    # print('User {} failed to log in through page {}'.format(credentials['username'],request.META.get('HTTP_REFERER')))
    uname=None
    uemail=None
    ip_address = request.META.get('REMOTE_ADDR') 
    try: 
        userobject = User.objects.get(username=credentials['username'])
    except User.DoesNotExist:
        userobject=None
        uname=credentials['username']
    try: 
        userdetail =UserDetails.objects.get(user_email=credentials['username']) 
    except UserDetails.DoesNotExist:
        userdetail=None
        uname=credentials['username']
        uemail=credentials['username']
    UserActivity.objects.create(user=userobject,username=uname,userdetails=userdetail,useremail=uemail, action_type='login_failed', ip_address=ip_address)  
@receiver(user_logged_out)
def log_user_logout(sender,user, request, **kwargs):
    # print('User {} logged out through page {}'.format(user.username,request.META.get('HTTP_REFERER')))
    ip_address = request.META.get('REMOTE_ADDR')
    userdetail =UserDetails.objects.get(user_id=user.id) 
    UserActivity.objects.create(user=user,userdetails=userdetail, action_type='logout', ip_address=ip_address)  