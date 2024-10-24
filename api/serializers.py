from rest_framework import serializers
from site_engineer.models import EngineerReport
from django.contrib.auth.models import User
from reception.models import ReceptionReport
from propval.models import UserDetails,Banks
from reporter.models import ReporterReport

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

class ReceptionSerializer(serializers.HyperlinkedModelSerializer):
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


