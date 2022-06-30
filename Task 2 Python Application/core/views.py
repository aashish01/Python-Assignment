from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from app_authentication.models import *
from rest_framework.permissions import IsAuthenticated

class DoctorList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            ReceptionistProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        objs = DoctorProfile.objects.all()
        if len(objs)>0:
            return Response({
                "error": False,
                "data": DoctorSerializer(objs, many=True, context={'request': request}).data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": False,
                "data": "No Doctor List Found.",
                "status": status.HTTP_204_NO_CONTENT
            }, status=status.HTTP_204_NO_CONTENT)


class PatientView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            ReceptionistProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        objs = Patient.objects.all()
        if len(objs)>0:
            return Response({
                "error": False,
                "data": PatientListSerializer(objs, many=True, context={'request': request}).data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": False,
                "data": "No Patient List Found.",
                "status": status.HTTP_204_NO_CONTENT
            }, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "error": False,
            "data": "Patient has been created.",
            "status": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)
        return Response({
            "error": True,
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            if 'slug' in request.data:
                obj = Patient.objects.get(slug=request.data["slug"])
            else:
                obj = Patient.objects.get(id=request.data["id"])  
        except:
            return Response({
                    "error": True,
                    "data": "Patient id or slug required.",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PatientSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "error": False,
                "data": "Patient has been updated.",
                "status": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
    
    def delete(self, request):
        try:
            if 'slug' in request.data:
                obj = Patient.objects.get(slug=request.data["slug"])
            else:
                obj = Patient.objects.get(id=request.data["id"])  
        except:
            return Response({
                    "error": True,
                    "data": "Patient id or slug required.",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
        obj.delete()
        return Response({
            "error": False,
            "data": "Patient has been deleted.",
            "status": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
        



class AppointmentView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            user =ReceptionistProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        try:
            patient = Patient.objects.get(slug=request.data['patient_slug'])
            doctor = DoctorProfile.objects.get(slug=request.data['doctor_slug'])
        except Exception as e:
            return Response({'error': True, 'data': str(e) +' '+ 'required'},status=status.HTTP_400_BAD_REQUEST)
        try:
            appoinment_date = request.data['appoinment_date']
            appoinment_time = request.data['appoinment_time']
            description = request.data['description']
        except Exception as e:
            return Response({'error': True, 'data': str(e) +' '+ 'required'},status=status.HTTP_400_BAD_REQUEST)
        try:
            appoinmentObj = Appointment.objects.create(
                appoinment_date=appoinment_date,
                appoinment_time=appoinment_time,
                description = description,
                patient = patient,
                doctor = doctor,
                issued_by = user
            )
            appoinmentObj.save()
            return Response({'error': True, 'data':'Appoinment Created.',"status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': True, 'data':'Check entired fields is vaild.',"status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)
    


class ActiveAppoinmantList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            user =DoctorProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        obj = Appointment.objects.filter(doctor=user.id,status=True)
        if len(obj)>0:
            appointment_list={
                'error':False,
                'data':AppointmentSerializer(obj, many=True, context={'request': request}).data,
                'status':status.HTTP_200_OK
            }
            return Response(appointment_list,status=status.HTTP_201_CREATED)
        else:
            return Response({'error': True, 'data':'No Active Appoinment Not Found.',"status":status.HTTP_204_NO_CONTENT},status=status.HTTP_204_NO_CONTENT)


class InAppoinmantList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            user =DoctorProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        obj = Appointment.objects.filter(doctor=user.id,status=False)
        if len(obj)>0:
            appointment_list={
                'error':False,
                'data':AppointmentSerializer(obj, many=True, context={'request': request}).data,
                'status':status.HTTP_200_OK
            }
            return Response(appointment_list,status=status.HTTP_201_CREATED)
        else:
            return Response({'error': True, 'data':'Inactive Appoinment Not Found.',"status":status.HTTP_204_NO_CONTENT},status=status.HTTP_204_NO_CONTENT)



class UpdateAppoinments(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            user =DoctorProfile.objects.get(user__id=request.user.id)
        except:
            return Response({
                "error": False,
                "data": 'Unauthorized to access data.',
                "status": status.HTTP_401_UNAUTHORIZED
            }, status=status.HTTP_401_UNAUTHORIZED)
        try:
            slug = request.data['slug']
        except Exception as e:
            return Response({'error': True, 'data': str(e) +' '+ 'required'},status=status.HTTP_400_BAD_REQUEST)
        try:
            obj=Appointment.objects.get(slug=slug)
            if obj.status!=False:
                obj.status=False
                obj.save()
                return Response({'error': False, 'data':'Appoinment Closed.',"status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
            else:
                return Response({'error': True, 'data':'Appoinment already Closed.',"status":status.HTTP_208_ALREADY_REPORTED},status=status.HTTP_208_ALREADY_REPORTED)
        except Exception as e:
            return Response({'error': True, 'data':'Appoinment not Found.',"status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)