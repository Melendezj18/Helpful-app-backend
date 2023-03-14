from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ..models.house import House
from ..serializers import HouseSerializer, HouseReadSerializer

class HousesView(generics.ListCreateAPIView):
    """
    A view for seeing all houses and creating a single house
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = HouseSerializer

    def get(self, request):
        '''Index request'''
        houses = House.objects.filter(owner=request.user.id)
        serializer = HouseReadSerializer(houses, many=True)
        return Response({'houses': serializer.data})

    def post(self, request):
        '''Create request'''
        request.data['house']['owner'] = request.user.id
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /houses/id


class HouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HouseSerializer

    def get(self, request, pk):
        '''Show request'''
        house = get_object_or_404(House, pk=pk)
        if not request.user.id == house.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this house')
        serializer = HouseReadSerializer(house)
        return Response(serializer.data)

    def patch(self, request, pk):
        '''Update Request'''
        house = get_object_or_404(House, pk=pk)
        if not request.user.id == house.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this house')
        request.data['house']['owner'] = request.user.id
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Delete Request'''
        house = get_object_or_404(House, pk=pk)
        if not request.user.id == house.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this house')
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
