from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle

from .serializers import ContactAPI_Serializer
from .models import Contact

# Create your views here.
class Category_Vacancy_APIViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.filter(status=True)
    serializer_class = ContactAPI_Serializer
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]   
    lookup_field = 'slug'
    
    
    
    