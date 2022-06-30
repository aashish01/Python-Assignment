from dataclasses import fields
from rest_framework import serializers
from .models import *
from app_authentication.models import *



class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields =('id','slug','name')

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    
    class Meta:
        model = DoctorProfile
        fields = ('id','slug','fullname','address','phone')
    
    def get_fullname(self, obj):
        return obj.user.name
    
    def get_address(self, obj):
        return obj.user.address

    def get_phone(self, obj):
        return obj.user.phone
    

class PatientDetails(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields =('id','slug','name','dob','address','phone')

class IssuedBy(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = ReceptionistProfile
        fields=('id','slug','email','name')
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email


class AppointmentSerializer(serializers.ModelSerializer):
    patient_details = serializers.SerializerMethodField()
    receptionist_details = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id','slug','patient_details','appoinment_date','appoinment_time','description','receptionist_details','created_at','updated_at')

    def get_patient_details(self,obj):
        request = self.context.get('request')
        return PatientDetails(obj.patient,context={'request':request}).data
    
    def get_receptionist_details(self,obj):
        request = self.context.get('request')
        return IssuedBy(obj.issued_by,context={'request':request}).data