from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('patients/',PatientView.as_view(),name='patients'),
    path('getdoctors/',DoctorList.as_view(),name='doctors-list'),
    path('appoinments/',AppointmentView.as_view(),name='appoinments'),
    path('complete/appoinments/',UpdateAppoinments.as_view(),name="update-appoinments"),
    path('active/appoinments/',ActiveAppoinmantList.as_view(),name='active-appoinments'),
    path('inactive/appoinments/',InAppoinmantList.as_view(),name='inactive-appoinments'),
]