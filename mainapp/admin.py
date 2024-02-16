from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class Contact_Admin(admin.ModelAdmin):
    list_display = ('full_name', 'group','school', 'phone_number','status', 'created_on')
    list_filter = ('group', 'status', 'created_on')
    search_fields = ('full_name','school', 'phone_number')
    list_editable = ('status', )
    

