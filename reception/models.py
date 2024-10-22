from django.db import models
from django.contrib.auth.models import User
from propval.models import UserDetails

# Create your models here.
class ReceptionReport(models.Model):
    applicationdate = models.DateTimeField(null=True)
    applicationnumber = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    bankname = models.CharField(max_length=50,null=True)
    bankid = models.IntegerField(null=True)
    bankvertical = models.CharField(max_length=50,null=True)
    add1 = models.CharField(max_length=100, null=True, default="Gwalior")
    add2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30,null=True)
    zip = models.CharField(max_length=6,null=True)
    country = models.CharField(max_length=20,null=True)
    phonenumber = models.CharField(max_length=10,null=True)
    visitingperson = models.IntegerField(null=True)    
    reportperson = models.IntegerField(null=True)
    visitingpersonname = models.CharField(max_length=50,null=True)    
    reportpersonname = models.CharField(max_length=50,null=True)
    engineer = models.CharField(max_length=10, null=True)
    reporter = models.CharField(max_length=10, null=True)
    priority = models.BooleanField(default=False)
    engineerholdcause = models.TextField(blank=True, null=True)
    reporterholdcause = models.TextField(null=True, blank=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

class Document(models.Model):
    application_number = models.CharField(max_length=20, default='0')
    file_path = models.CharField(max_length=255,default='media')
    file_name = models.CharField(max_length=255,default='null')
    reception_idno = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=20,null=True)
    usersdetailsid = models.IntegerField(null=True, blank=True)
    platform = models.CharField(max_length=20,null=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.file_name    
    