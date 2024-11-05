from django.db import models
from reception.models import ReceptionReport
from propval.models import UserDetails
from django.contrib.auth.models import User

# Create your models here.

class EngineerReport(models.Model):
    applicationnumber = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    visitinpresence = models.CharField(max_length=30,null=True)
    bankname = models.CharField(max_length=50)
    bankid = models.IntegerField(null=True)
    casetype = models.CharField(max_length=50)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    east = models.CharField(max_length=50,null=True)
    west = models.CharField(max_length=50,null=True)
    north = models.CharField(max_length=50,null=True)
    south = models.CharField(max_length=50,null=True)
    gfarea = models.CharField(max_length=10,null=True)
    ffarea = models.CharField(max_length=10,null=True)
    sfarea = models.CharField(max_length=10,null=True)
    tfarea = models.CharField(max_length=10,null=True)
    propertyage = models.CharField(max_length=3,null=True)
    landrate = models.CharField(max_length=10,null=True)    
    Occupant = models.CharField(max_length=50,null=True)
    rented = models.CharField(max_length=50, null=True)
    landmark = models.CharField(max_length=100,null=True)
    roadwidth = models.CharField(max_length=10,null=True)
    hightensionline = models.BooleanField(null=True)
    railwayline = models.BooleanField(null=True)
    nala = models.BooleanField(null=True)
    river = models.BooleanField(null=True)
    pahad = models.BooleanField(null=True)
    roadcomesunderroadbinding = models.BooleanField(null=True)
    propertyaccessissue = models.BooleanField(null=True)
    othercheck = models.BooleanField(null=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    reporter = models.CharField(max_length=10, null=True)
    reportersubmitdate = models.DateTimeField(null=True, blank=True)
    receptionid = models.ForeignKey(ReceptionReport, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.BooleanField(default=False,null=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    reporterholdcause = models.TextField(blank=True, null=True)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
class ArchieveEngineerReport(models.Model):
    applicationnumber = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    visitinpresence = models.CharField(max_length=30,null=True)
    bankname = models.CharField(max_length=50)
    bankid = models.IntegerField(null=True)
    casetype = models.CharField(max_length=50)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    east = models.CharField(max_length=50,null=True)
    west = models.CharField(max_length=50,null=True)
    north = models.CharField(max_length=50,null=True)
    south = models.CharField(max_length=50,null=True)
    gfarea = models.CharField(max_length=10,null=True)
    ffarea = models.CharField(max_length=10,null=True)
    sfarea = models.CharField(max_length=10,null=True)
    tfarea = models.CharField(max_length=10,null=True)
    propertyage = models.CharField(max_length=3,null=True)
    landrate = models.CharField(max_length=10,null=True)    
    Occupant = models.CharField(max_length=50,null=True)
    rented = models.CharField(max_length=50, null=True)
    landmark = models.CharField(max_length=100,null=True)
    roadwidth = models.CharField(max_length=10,null=True)
    hightensionline = models.BooleanField(null=True)
    railwayline = models.BooleanField(null=True)
    nala = models.BooleanField(null=True)
    river = models.BooleanField(null=True)
    pahad = models.BooleanField(null=True)
    roadcomesunderroadbinding = models.BooleanField(null=True)
    propertyaccessissue = models.BooleanField(null=True)
    othercheck = models.BooleanField(null=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    reporter = models.CharField(max_length=10, null=True)
    reportersubmitdate = models.DateTimeField(null=True, blank=True)
    receptionid = models.ForeignKey(ReceptionReport, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.BooleanField(default=False,null=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    reporterholdcause = models.TextField(blank=True, null=True)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archievedate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
