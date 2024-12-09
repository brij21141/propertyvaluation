from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.

#class CustomUser(AbstractUser):
  #  userType = models.IntegerField(unique=True)
# class UserData(models.Model):
#    username=models.CharField(max_length=50)
#    email=models.CharField(max_length=50)
#    staffstatus=models.BooleanField



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,null=True)
    user_email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)  # Allow null and blank values
    phone = models.CharField(max_length=10, null=True, blank=True)
    add1 = models.CharField(max_length=100, null=True, blank=True)
    add2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    zip = models.CharField(max_length=6, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    profileimage = models.ImageField(null=True, blank=True,upload_to="profile/")
    role = models.CharField(max_length=30, null=True, blank=True)
    bankname = models.CharField(max_length=50, null=True)
    bankacno = models.CharField(max_length=20, null=True)
    bankacnoconf = models.CharField(max_length=20, null=True)
    ifsccode = models.CharField(max_length=12,null=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.user_email = self.user.email
        super().save(*args, **kwargs)


class CompanyProfile(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    zip = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=20,null=True, blank=True)
    contact_no = models.CharField(max_length=15,null=True, blank=True)
    std = models.CharField(max_length=4,null=True, blank=True)
    phone = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    gstin = models.CharField(max_length=15,null=True, blank=True)
    pan = models.CharField(max_length=10,null=True, blank=True)
    bankname = models.CharField(max_length=50,null=True, blank=True)
    bankacno = models.CharField(max_length=50,null=True, blank=True)
    ifsc = models.CharField(max_length=15,null=True, blank=True)
    terms = models.TextField(null=True, blank=True)
    
    profileimage = models.ImageField(null=True, blank=True,upload_to="profile/")
    def __str__(self):
        return self.name

class Banks(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    add1 = models.TextField(null=True, blank=True)
    add2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    zip = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=20,null=True, blank=True)
    contact_no = models.CharField(max_length=15,null=True, blank=True)
    std = models.CharField(max_length=4,null=True, blank=True)
    landline = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    gstin = models.CharField(max_length=15,null=True, blank=True)
    pan = models.CharField(max_length=10,null=True, blank=True)
    internalrate = models.FloatField(null=True, blank=True)
    externalrate = models.FloatField(null=True, blank=True)
    partamount = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.id)

class UserActivity(models.Model):  
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True) 
    username=models.CharField(max_length=80,null=True)
    userdetails = models.ForeignKey(UserDetails, on_delete=models.DO_NOTHING,null=True) 
    useremail=models.CharField(max_length=80,null=True)
    action_type = models.CharField(max_length=50)  # e.g. "login", "logout", "login_failed"  
    timestamp = models.DateTimeField(auto_now_add=True)  
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Optional

class Impdoc(models.Model):  
    narration=models.CharField(max_length=200,null=True)
    linkurl=models.CharField(max_length=200,null=True)
    userdetails = models.ForeignKey(UserDetails, on_delete=models.DO_NOTHING,null=True)
    active = models.BooleanField(default=True) 
    timestamp = models.DateTimeField(auto_now_add=True)  
    