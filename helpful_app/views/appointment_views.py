from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ..models.appointment import Appointment
from ..serializers import AppointmentSerializer, AppointmentReadSerializer


class AppointmentsView(generics.ListCreateAPIView):
    """
    A view for seeing all appointments and creating a single appointment

    /library/appointments/
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get(self, request):
        '''Index request'''
        appointments = Appointment.objects.filter(owner=request.user.id)
        serializer = AppointmentReadSerializer(appointments, many=True)
        return Response({'appointments': serializer.data})

    def post(self, request):
        '''Create request'''
        request.data['appointment']['owner'] = request.user.id
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /appointments/id


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get(self, request, pk):
        '''Show request'''
        appointment = get_object_or_404(Appointment, pk=pk)
        if not request.user.id == appointment.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this appointment')
        serializer = AppointmentReadSerializer(appointment)
        return Response(serializer.data)

    def patch(self, request, pk):
        '''Update Request'''
        appointment = get_object_or_404(Appointment, pk=pk)
        if not request.user.id == appointment.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this appointment')
        request.data['appointment']['owner'] = request.user.id
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Delete Request'''
        appointment = get_object_or_404(Appointment, pk=pk)
        if not request.user.id == appointment.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this appointment')
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

