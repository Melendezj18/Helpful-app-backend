from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.house import House
from ..serializers import HouseSerializer, HouseReadSerializer

class HousesView(generics.ListCreateAPIView):
    """
    A view for seeing all houses and creating a single house
    """
    serializer_class = HouseSerializer

    def get(self, request):
        '''Index request'''
        houses = House.objects.all()
        serializer = HouseReadSerializer(houses, many=True)
        return Response({'houses': serializer.data})

    def post(self, request):
        '''Create request'''
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /houses/id


class HouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer

    def get(self, request, pk):
        '''Show request'''
        house = get_object_or_404(House, pk=pk)
        serializer = HouseReadSerializer(house)
        return Response(serializer.data)

    def patch(self, request, pk):
        '''Update Request'''
        house = get_object_or_404(House, pk=pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''Delete Request'''
        house = get_object_or_404(House, pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
