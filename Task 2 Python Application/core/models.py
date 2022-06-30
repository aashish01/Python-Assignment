from django.db import models
from Appointment.utils import name__slug_generator,random_slug_generator
from django.db.models.signals import pre_save
from app_authentication.models import *
import uuid

# FOR GENERATING SLUGS
def name_slug_Generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = name__slug_generator(instance)

def random_slug_Generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = random_slug_generator(instance)

# Create your models here.
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=155, null=True,
                            blank=True, help_text="This will auto generate its value")
    name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table = "tbl_patient_profile"
        verbose_name = 'Patient Profile'
        verbose_name_plural ="Patient's Profile"
pre_save.connect(name_slug_Generator,sender=Patient)

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=155, null=True,
                            blank=True, help_text="This will auto generate its value")
    appoinment_date = models.CharField(help_text='appoinment date',max_length=200)
    appoinment_time = models.CharField(help_text='appoinment time',max_length=200)
    doctor = models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    issued_by = models.ForeignKey(ReceptionistProfile,on_delete=models.CASCADE)
    description = models.TextField(help_text="Description of appointment")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.appoinment_date)
    
    class Meta:
        db_table = "tbl_appoinment_details"
        verbose_name = 'Appoinment Detail'
        verbose_name_plural ="Appoinment Details"
pre_save.connect(random_slug_Generator,sender=Appointment)