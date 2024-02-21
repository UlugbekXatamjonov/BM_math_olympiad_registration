from rest_framework import serializers
from .models import Contact

class ContactAPI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('full_name', 'group', 'school', "phone_number")


class StatisticsAPI_Serializer(serializers.Serializer):
    """ Statistics API Serializer """
    class_number = serializers.CharField() # Sinf raqami
    aplications_count = serializers.IntegerField() # Sinf bo'yicha tushgan arizalar soni
        
            