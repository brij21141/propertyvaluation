from rest_framework import serializers
from site_engineer.models import EngineerReport,EngAttendance,Occupants,Floordetails,EngDynamicdValue,HistoryEngineerReport,HistoryFloordetails,HistoryOccupants,HistoryEngDynamicdValue
from django.contrib.auth.models import User
from reception.models import ReceptionReport,Document
from propval.models import UserDetails,Banks,EngDynamicField,EngFormOptionValues,EngFormsubOptionValues
from reporter.models import ReporterReport

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

class DynValueSerializer(serializers.ModelSerializer):
    
    id = serializers.ReadOnlyField()
    class Meta:
        model = EngDynamicdValue
        fields = ('id', 'engreportid_id', 'input_field_id','value','subvalue')

# class DynamicValueSerializer(serializers.HyperlinkedModelSerializer):
#     dynamic_values = DynValueSerializer(many=True, read_only=True)
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model = EngDynamicField
#         # fields = "__all__"
#         fields = ('id', 'label', 'input_type','active','suboption','form_type','dynamic_values') 
class DynamicfieldSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = EngDynamicField
        fields = "__all__"
       
# class DynamicValueSerializer(serializers.ModelSerializer):
#     input_field = DynamicfieldSerializer(read_only=True)
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model = EngDynamicdValue
#         fields = ('id', 'engreportid_id', 'input_field_id','value','subvalue','input_field')
class SuboptionvaluesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = EngFormsubOptionValues
        # fields = "__all__"
        fields = ('id', 'name') 
class OptionvaluesSerializer(serializers.ModelSerializer):
    sub_options = SuboptionvaluesSerializer(many=True, read_only=True)
    id = serializers.ReadOnlyField()
    class Meta:
        model = EngFormOptionValues
        # fields = "__all__"
        fields = ('id', 'opt_value', 'sub_options','eng_dynamic_field')

class ReceptionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = ReceptionReport
        fields = "__all__"

class ReceptionfieldsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReceptionReport
        fields = ('id','phonenumber','visitingpersonname','reportpersonname')
# this consist reception fields also so problem in posting new api to post is below
class EngineerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # receptionid = serializers.ReadOnlyField()
    # success = serializers.BooleanField(default=True)
    receptionid=ReceptionfieldsSerializer()
    class Meta:
        model=EngineerReport
        fields = "__all__"
# to create a engineering report record this is api
class EngineerCreateSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model=EngineerReport
        fields = "__all__" 
class HistoryEngineerCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=HistoryEngineerReport
        fields = "__all__" 
class HistoryFloordetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=HistoryFloordetails
        fields = "__all__" 
class HistoryOccupantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=HistoryOccupants
        fields = "__all__" 
class HistoryEngDynamicdValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=HistoryEngDynamicdValue
        fields = "__all__" 
class EngineerAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=EngAttendance
        fields = "__all__" 

class BankSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Banks
        fields = "__all__"      
           
class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    receptionid=ReceptionfieldsSerializer()
    bankid=BankSerializer()
    class Meta:
        model=ReporterReport
        fields = "__all__" 


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields = "__all__" 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserdetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()

class FileUploadSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField() 
    class Meta:
        model = Document
        fields = "__all__"
class OccupantSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField() 
    class Meta:
        model = Occupants
        fields = "__all__"
class FloorSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField() 
    class Meta:
        model = Floordetails
        fields = "__all__"
# class FloorSerializer(serializers.ModelSerializer):  
#     class Meta:  
#         model = Floor  
#         fields = ['flname', 'fldetails', 'flarea']  

# class EngineereditSerializer(serializers.ModelSerializer):  
#     floors = FloorSerializer(many=True)  

#     class Meta:  
#         model = EngineerReport  
#         fields = [  
#             'id',   
#             'application_number',   
#             'name',   
#             'visit_in_presence',   
#             'bank_name',   
#             'case_type',   
#             'add1',   
#             'add2',   
#             'city',   
#             'region',   
#             'zip_code',   
#             'country',   
#             'east',   
#             'west',   
#             'north',   
#             'south',   
#             'floors'  
#         ]  