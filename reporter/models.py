from django.db import models
from django.contrib.auth.models import User
from reception.models import ReceptionReport,ArchieveReceptionReport
from propval.models import Banks

class ReporterReport(models.Model):
    inspectiondate = models.DateTimeField(null=True)
    applicationnumber = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    docholdername = models.CharField(max_length=30,null=True)
    propertytype = models.CharField(max_length=30,null=True)
    add1 = models.CharField(max_length=100, null=True, default="Gwalior")
    add2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30,null=True)
    zip = models.CharField(max_length=6,null=True)
    country = models.CharField(max_length=20,null=True,default='India')
    landmark = models.CharField(max_length=100,null=True)
    ladd1 = models.CharField(max_length=100, null=True, default="Gwalior")
    ladd2 = models.CharField(max_length=100, null=True)
    lcity = models.CharField(max_length=30, null=True)
    lregion = models.CharField(max_length=30,null=True)
    lzip = models.CharField(max_length=6,null=True)
    lcountry = models.CharField(max_length=20,null=True,default='India')
    wardlandno = models.CharField(max_length=20,null=True)
    approachroadwidth =models.CharField(max_length=20,null=True)
    plotdem = models.CharField(max_length=20,null=True)
    vicinity=models.CharField(max_length=10,null=True)
    propertylocation=models.CharField(max_length=100,null=True)
    propertyidentification=models.CharField(max_length=100,null=True)
    connectivityinfrastructure=models.CharField(max_length=100,null=True)
    railwaystation=models.CharField(max_length=100,null=True)
    busstop=models.CharField(max_length=100,null=True)
    hospital=models.CharField(max_length=100,null=True)
    nearestlandmark=models.CharField(max_length=100,null=True)
    typeusageproperty=models.CharField(max_length=100,null=True)
    additionalamenities=models.CharField(max_length=100,null=True)
    legalstatusproperty=models.CharField(max_length=100,null=True)
    typepremises=models.CharField(max_length=100,null=True)
    taxationmaintancecost =models.CharField(max_length=100,null=True)
    rentingpotential=models.CharField(max_length=100,null=True)
    marketrentals=models.CharField(max_length=100,null=True)
    occupiedby=models.CharField(max_length=100,null=True)
    ispropertyrented=models.CharField(max_length=100,null=True)
    listofoccupants=models.CharField(max_length=100,null=True)
    perdcboundryeast=models.CharField(max_length=100,null=True)
    perdcboundrywset=models.CharField(max_length=100,null=True)
    perdcboundrynorth=models.CharField(max_length=100,null=True)
    perdcboundrysouth=models.CharField(max_length=100,null=True)
    perstboundryeast=models.CharField(max_length=100,null=True)
    perstboundrywest=models.CharField(max_length=100,null=True)
    perstboundrynorth=models.CharField(max_length=100,null=True)
    perstboundrysouth=models.CharField(max_length=100,null=True)
    typestructure=models.CharField(max_length=100,null=True)
    nofloors=models.CharField(max_length=100,null=True)
    nowings=models.CharField(max_length=100,null=True)
    nouniteachfloor=models.CharField(max_length=100,null=True)
    nolifteachwing=models.CharField(max_length=100,null=True)
    ageproperty=models.CharField(max_length=100,null=True)
    futurelife=models.CharField(max_length=100,null=True)
    exterior=models.CharField(max_length=100,null=True)
    internalcomposition=models.CharField(max_length=100,null=True)
    constructionquality=models.CharField(max_length=100,null=True)
    beamcolumnstru=models.CharField(max_length=100,null=True)
    commonarearemark=models.CharField(max_length=100,null=True)
    otherobservation=models.CharField(max_length=100,null=True)
    floornfinish=models.CharField(max_length=100,null=True)
    roofingnterracing=models.CharField(max_length=100,null=True)
    nooflifts=models.CharField(max_length=10,null=True)
    qualityfixing=models.CharField(max_length=100,null=True)
    constasperaprove=models.CharField(max_length=10,null=True)
    aprnodate=models.CharField(max_length=100,null=True)
    constnodate=models.CharField(max_length=100,null=True)
    violationifany=models.CharField(max_length=100,null=True)
    confirmlocalbilaws=models.CharField(max_length=100,null=True)
    otherverifieddoc=models.CharField(max_length=100,null=True)
    carpetareaflwise=models.CharField(max_length=100,null=True)
    aprovbuaflwise=models.CharField(max_length=100,null=True)
    govtapprovalrate=models.CharField(max_length=10,null=True)
    recomendrate=models.CharField(max_length=100,null=True)
    mktvalueinfig=models.CharField(max_length=10,null=True)
    mktvalueinwords=models.CharField(max_length=100,null=True)
    forcessalesless=models.CharField(max_length=100,null=True)
    arearatepsft=models.CharField(max_length=100,null=True)
    areavalueinfig=models.CharField(max_length=100,null=True)
    areavalueinwords=models.CharField(max_length=100,null=True)
    landarea=models.CharField(max_length=100,null=True)
    govtaprovelandrate=models.CharField(max_length=100,null=True)
    recommendedlandrate=models.CharField(max_length=100,null=True)
    landvalue=models.CharField(max_length=100,null=True)
    actualbua=models.CharField(max_length=100,null=True)
    asperpermissionbua=models.CharField(max_length=100,null=True)
    constcostperaminity=models.CharField(max_length=100,null=True)
    totalconstvalue=models.CharField(max_length=100,null=True)
    depreciatedconstvalue=models.CharField(max_length=100,null=True)
    landvaluedepndepconstvalueinfig=models.CharField(max_length=100,null=True)
    landvaluedepndepconstvalueinword=models.CharField(max_length=100,null=True)
    forcesalevaluepersqft=models.CharField(max_length=100,null=True)
    forcesvalueinfig=models.CharField(max_length=100,null=True)
    forcesvalueinword=models.CharField(max_length=100,null=True)
    marketibility=models.CharField(max_length=10,null=True)
    valuationresult=models.CharField(max_length=10,null=True)
    remark=models.CharField(max_length=100,null=True)
    # receptionid=models.IntegerField(null=True)
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    bankid = models.ForeignKey(Banks,on_delete=models.SET_NULL, null=True, blank=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def __str__(self):
     return str(self.id)
class ArchieveReporterReport(models.Model):
    inspectiondate = models.DateTimeField(null=True)
    applicationnumber = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    docholdername = models.CharField(max_length=30,null=True)
    propertytype = models.CharField(max_length=30,null=True)
    add1 = models.CharField(max_length=100, null=True, default="Gwalior")
    add2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30,null=True)
    zip = models.CharField(max_length=6,null=True)
    country = models.CharField(max_length=20,null=True,default='India')
    landmark = models.CharField(max_length=100,null=True)
    ladd1 = models.CharField(max_length=100, null=True, default="Gwalior")
    ladd2 = models.CharField(max_length=100, null=True)
    lcity = models.CharField(max_length=30, null=True)
    lregion = models.CharField(max_length=30,null=True)
    lzip = models.CharField(max_length=6,null=True)
    lcountry = models.CharField(max_length=20,null=True,default='India')
    wardlandno = models.CharField(max_length=20,null=True)
    approachroadwidth =models.CharField(max_length=20,null=True)
    plotdem = models.CharField(max_length=20,null=True)
    vicinity=models.CharField(max_length=10,null=True)
    propertylocation=models.CharField(max_length=100,null=True)
    propertyidentification=models.CharField(max_length=100,null=True)
    connectivityinfrastructure=models.CharField(max_length=100,null=True)
    railwaystation=models.CharField(max_length=100,null=True)
    busstop=models.CharField(max_length=100,null=True)
    hospital=models.CharField(max_length=100,null=True)
    nearestlandmark=models.CharField(max_length=100,null=True)
    typeusageproperty=models.CharField(max_length=100,null=True)
    additionalamenities=models.CharField(max_length=100,null=True)
    legalstatusproperty=models.CharField(max_length=100,null=True)
    typepremises=models.CharField(max_length=100,null=True)
    taxationmaintancecost =models.CharField(max_length=100,null=True)
    rentingpotential=models.CharField(max_length=100,null=True)
    marketrentals=models.CharField(max_length=100,null=True)
    occupiedby=models.CharField(max_length=100,null=True)
    ispropertyrented=models.CharField(max_length=100,null=True)
    listofoccupants=models.CharField(max_length=100,null=True)
    perdcboundryeast=models.CharField(max_length=100,null=True)
    perdcboundrywset=models.CharField(max_length=100,null=True)
    perdcboundrynorth=models.CharField(max_length=100,null=True)
    perdcboundrysouth=models.CharField(max_length=100,null=True)
    perstboundryeast=models.CharField(max_length=100,null=True)
    perstboundrywest=models.CharField(max_length=100,null=True)
    perstboundrynorth=models.CharField(max_length=100,null=True)
    perstboundrysouth=models.CharField(max_length=100,null=True)
    typestructure=models.CharField(max_length=100,null=True)
    nofloors=models.CharField(max_length=100,null=True)
    nowings=models.CharField(max_length=100,null=True)
    nouniteachfloor=models.CharField(max_length=100,null=True)
    nolifteachwing=models.CharField(max_length=100,null=True)
    ageproperty=models.CharField(max_length=100,null=True)
    futurelife=models.CharField(max_length=100,null=True)
    exterior=models.CharField(max_length=100,null=True)
    internalcomposition=models.CharField(max_length=100,null=True)
    constructionquality=models.CharField(max_length=100,null=True)
    beamcolumnstru=models.CharField(max_length=100,null=True)
    commonarearemark=models.CharField(max_length=100,null=True)
    otherobservation=models.CharField(max_length=100,null=True)
    floornfinish=models.CharField(max_length=100,null=True)
    roofingnterracing=models.CharField(max_length=100,null=True)
    nooflifts=models.CharField(max_length=10,null=True)
    qualityfixing=models.CharField(max_length=100,null=True)
    constasperaprove=models.CharField(max_length=10,null=True)
    aprnodate=models.CharField(max_length=100,null=True)
    constnodate=models.CharField(max_length=100,null=True)
    violationifany=models.CharField(max_length=100,null=True)
    confirmlocalbilaws=models.CharField(max_length=100,null=True)
    otherverifieddoc=models.CharField(max_length=100,null=True)
    carpetareaflwise=models.CharField(max_length=100,null=True)
    aprovbuaflwise=models.CharField(max_length=100,null=True)
    govtapprovalrate=models.CharField(max_length=10,null=True)
    recomendrate=models.CharField(max_length=100,null=True)
    mktvalueinfig=models.CharField(max_length=10,null=True)
    mktvalueinwords=models.CharField(max_length=100,null=True)
    forcessalesless=models.CharField(max_length=100,null=True)
    arearatepsft=models.CharField(max_length=100,null=True)
    areavalueinfig=models.CharField(max_length=100,null=True)
    areavalueinwords=models.CharField(max_length=100,null=True)
    landarea=models.CharField(max_length=100,null=True)
    govtaprovelandrate=models.CharField(max_length=100,null=True)
    recommendedlandrate=models.CharField(max_length=100,null=True)
    landvalue=models.CharField(max_length=100,null=True)
    actualbua=models.CharField(max_length=100,null=True)
    asperpermissionbua=models.CharField(max_length=100,null=True)
    constcostperaminity=models.CharField(max_length=100,null=True)
    totalconstvalue=models.CharField(max_length=100,null=True)
    depreciatedconstvalue=models.CharField(max_length=100,null=True)
    landvaluedepndepconstvalueinfig=models.CharField(max_length=100,null=True)
    landvaluedepndepconstvalueinword=models.CharField(max_length=100,null=True)
    forcesalevaluepersqft=models.CharField(max_length=100,null=True)
    forcesvalueinfig=models.CharField(max_length=100,null=True)
    forcesvalueinword=models.CharField(max_length=100,null=True)
    marketibility=models.CharField(max_length=10,null=True)
    valuationresult=models.CharField(max_length=10,null=True)
    remark=models.CharField(max_length=100,null=True)
    # receptionid=models.IntegerField(null=True)
    lat = models.CharField(max_length=200,null=True,blank=True)
    lng = models.CharField(max_length=200,null=True,blank=True)
    placeid = models.CharField(max_length=200,null=True,blank=True)
    # receptionid = models.ForeignKey(ReceptionReport, on_delete=models.DO_NOTHING, null=True, blank=True)
    receptionid = models.ForeignKey(ArchieveReceptionReport, on_delete=models.DO_NOTHING,null=True, blank=True)
    # receptiontempid = models.IntegerField(null=True, blank=True)
    bankid = models.ForeignKey(Banks,on_delete=models.SET_NULL, null=True, blank=True)
    userdetailsid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    archieved = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archievedate = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
     return str(self.id)