from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response

# Create your views here.

class houseView(viewsets.ModelViewSet):
 
    serializer_class = houseSerializer
    queryset = House.objects.all()
class ListHouseView(ListAPIView):
    queryset= House.objects.all()
    serializer_class= houseSerializer

class CreateHouseView(CreateAPIView):
    queryset= House.objects.all()
    serializer_class= houseSerializer
    
class UpdateHouseView(UpdateAPIView): 
    queryset= House.objects.all()
    serializer_class= houseSerializer

class DeleteHouseView(DestroyAPIView):
    queryset= House.objects.all()
    serializer_class= houseSerializer
    
    
class meubleView(viewsets.ModelViewSet):
 
    serializer_class = meublesSerializer
    queryset = meubles.objects.all()
class ListMeubleView(ListAPIView):
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer

class CreateMeubleView(CreateAPIView):
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer
    
class UpdateMeubleView(UpdateAPIView): 
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer

class DeleteMeubleView(DestroyAPIView):
    queryset= meubles.objects.all()
    serializer_class= meublesSerializer    