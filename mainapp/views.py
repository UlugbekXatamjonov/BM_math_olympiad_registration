from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .serializers import ContactAPI_Serializer, StatisticsAPI_Serializer
from .models import Contact


# Create your views here.
class Category_Vacancy_APIViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.filter(status=True)
    serializer_class = ContactAPI_Serializer
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]   
    lookup_field = 'slug'
    
    
class Statistics_APIViewset(viewsets.ViewSet):
    """ Statistika uchun Viewset """
    def list(self, request):
        """ Sinflar kesimida tushgan arizalarni sanash va uni API ga aylantirish uchun mahsus funksiya. """
        class_counts = [] # sinflar soni
        for i in range(1, 12): # 1-11 gacha sinflar uchun sonli orqaliq shakillantirib olinadi
            class_number = str(i) # i-bu yerda "int" bo'lgani uchun uni endi "str" qilib olinyapdi
            # Modelning obyektlari orasidan kerakli sinfda yaratilgan obyektlar ajratib olinyapdi 
            aplications_count = Contact.objects.filter(group=class_number).count()
            # Ro'yhat ko'rinishida "sinf:undagi arizalar soni" ko'rinishi ma'lumot ro'yhatga qo'shilyapdi 
            class_counts.append({'class_number': class_number, 'aplications_count': aplications_count})
        
        # tayyor ma'lumotlar API qilinishi uchun serializerga yuborilyapdi
        serializer = StatisticsAPI_Serializer(class_counts, many=True)
        return Response(serializer.data)
    
    
    
    
    