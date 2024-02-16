from rest_framework import serializers
from .models import Contact

class ContactAPI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('full_name', 'group', 'school', "phone_number")



