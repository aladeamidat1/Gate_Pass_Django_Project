from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User ,House
from resident.serializers import HouseSerializer


# Create your views here.

@api_view()
def create_resident(request):
    return Response("create resident")

@api_view(['POST'])
def add_house(request):

    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, pk = serializer.validated_data['user'])
    if user.is_resident:
        House.objects.create(
            house_number = serializer.validated_data['house_number'],
            address = serializer.validated_data['address'],
            user = user
        )

        return Response(data={"message": "house added"}, status=status.HTTP_201_CREATED)
    return Response(data={"message":"Not Authorized"} , status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def view_house(request, house_number):
    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, pk = serializer.validated_data['user'])
    if user.is_resident:
        house = House.objects.get(
            house_number = house_number)
        return Response(data={"message": "successful"}, status=status.HTTP_201_CREATED)
    return Response(data={"message":"Not Authorized"} , status=status.HTTP_403_FORBIDDEN)



