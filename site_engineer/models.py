from django.db import models
from reception.models import ReceptionReport,ArchieveReceptionReport
from propval.models import UserDetails,EngDynamicField
from django.contrib.auth.models import User

# Create your models here.

class EngineerReport(models.Model):
    applicationnumber = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    visitinpresence = models.CharField(max_length=30,null=True)
    bankname = models.CharField(max_length=50)
    bankid = models.IntegerField(null=True)
    casetype = models.CharField(max_length=50)
    add1 = models.CharField(max_length=250)
    add2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    east = models.CharField(max_length=50,null=True)
    west = models.CharField(max_length=50,null=True)
    north = models.CharField(max_length=50,null=True)
    south = models.CharField(max_length=50,null=True)
    barea = models.CharField(max_length=10,null=True)
    gfarea = models.CharField(max_length=10,null=True)
    ffarea = models.CharField(max_length=10,null=True)
    sfarea = models.CharField(max_length=10,null=True)
    tfarea = models.CharField(max_length=10,null=True)
    frarea = models.CharField(max_length=10,null=True)
    fvarea = models.CharField(max_length=10,null=True)
    sxarea = models.CharField(max_length=10,null=True)
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
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    priority = models.BooleanField(default=False,null=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    reporterholdcause = models.TextField(blank=True, null=True)
    archieved = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
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
    add1 = models.CharField(max_length=250)
    add2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    east = models.CharField(max_length=50,null=True)
    west = models.CharField(max_length=50,null=True)
    north = models.CharField(max_length=50,null=True)
    south = models.CharField(max_length=50,null=True)
    barea = models.CharField(max_length=10,null=True)
    gfarea = models.CharField(max_length=10,null=True)
    ffarea = models.CharField(max_length=10,null=True)
    sfarea = models.CharField(max_length=10,null=True)
    tfarea = models.CharField(max_length=10,null=True)
    frarea = models.CharField(max_length=10,null=True)
    fvarea = models.CharField(max_length=10,null=True)
    sxarea = models.CharField(max_length=10,null=True)
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
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    # receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    receptionid = models.ForeignKey(ArchieveReceptionReport, on_delete=models.DO_NOTHING,null=True, blank=True)
    # receptiontempid = models.IntegerField(null=True, blank=True)
    priority = models.BooleanField(default=False,null=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    reporterholdcause = models.TextField(blank=True, null=True)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archievedate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    
class HistoryEngineerReport(models.Model):
    engreport = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='histories')  
    old_id = models.IntegerField(null=True)
    applicationnumber = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    visitinpresence = models.CharField(max_length=30,null=True)
    bankname = models.CharField(max_length=50)
    bankid = models.IntegerField(null=True)
    casetype = models.CharField(max_length=50)
    add1 = models.CharField(max_length=250)
    add2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    east = models.CharField(max_length=50,null=True)
    west = models.CharField(max_length=50,null=True)
    north = models.CharField(max_length=50,null=True)
    south = models.CharField(max_length=50,null=True)
    barea = models.CharField(max_length=10,null=True)
    gfarea = models.CharField(max_length=10,null=True)
    ffarea = models.CharField(max_length=10,null=True)
    sfarea = models.CharField(max_length=10,null=True)
    tfarea = models.CharField(max_length=10,null=True)
    frarea = models.CharField(max_length=10,null=True)
    fvarea = models.CharField(max_length=10,null=True)
    sxarea = models.CharField(max_length=10,null=True)
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
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    # receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    priority = models.BooleanField(default=False,null=True)
    # userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    reporterholdcause = models.TextField(blank=True, null=True)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

class Floordetails(models.Model):
    floorname = models.CharField(max_length=20,null=True)
    floordetail = models.CharField(max_length=200,null=True)
    floorarea = models.CharField(max_length=10,null=True)
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='floors')
    def __str__(self):
        return str(self.id)
class HistoryFloordetails(models.Model):
    floorname = models.CharField(max_length=20,null=True)
    floordetail = models.CharField(max_length=200,null=True)
    floorarea = models.CharField(max_length=10,null=True)
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='hsfloors')
    historyengreportid = models.ForeignKey(HistoryEngineerReport, related_name='historyfloors', on_delete=models.CASCADE)  
    def __str__(self):
        return str(self.id)

class Occupants(models.Model):
    occupantname = models.CharField(max_length=50,null=True)
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='occupants')
    def __str__(self):
        return str(self.id)

class HistoryOccupants(models.Model):
    occupantname = models.CharField(max_length=50,null=True)
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='hsoccupants')
    historyengreportid = models.ForeignKey(HistoryEngineerReport, related_name='historyoccupants', on_delete=models.CASCADE)  
    def __str__(self):
        return str(self.id)

class EngDynamicdValue(models.Model):  
    input_field = models.ForeignKey(EngDynamicField, on_delete=models.DO_NOTHING)  
    value = models.CharField(max_length=100,null=True)  
    subvalue = models.CharField(max_length=100,null=True)  
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='engdynamic')
    submitted_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"{self.input_field.label}: {self.value}"
    
class HistoryEngDynamicdValue(models.Model):  
    input_field = models.ForeignKey(EngDynamicField, on_delete=models.DO_NOTHING)  
    value = models.CharField(max_length=100,null=True)  
    subvalue = models.CharField(max_length=100,null=True)  
    engreportid = models.ForeignKey(EngineerReport, on_delete=models.DO_NOTHING,null=True, blank=True, related_name='hsengdynamic')
    hsengreportid = models.ForeignKey(HistoryEngineerReport, related_name='hsengdynamic', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"{self.input_field.label}: {self.value}"
    
class EngAttendance(models.Model):
    applicationnumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=30,null=True, blank=True)
    region = models.CharField(max_length=30,null=True, blank=True)
    zip = models.CharField(max_length=6,null=True, blank=True)
    country = models.CharField(max_length=20,null=True, blank=True)
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    indatetinme = models.DateTimeField(auto_now_add=True)
    outdatetinme = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return str(self.id)

    