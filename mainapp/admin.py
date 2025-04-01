from importlib import resources
from django.contrib import admin


from .models import Contact


from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ContactResource(resources.ModelResource):

    class Meta:
        model = Contact
        fields = ('full_name', 'group', 'school', 'phone_number', 'created_on' )


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    resource_classes = [ContactResource]
    
    