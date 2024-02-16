from django.db import models
from autoslug import AutoSlugField

# Create your models here.
GROUP = (
    ("1", '1'),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11")
)

class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ism familiya ")
    slug = AutoSlugField(populate_from = 'full_name', unique=True)
    group = models.CharField(max_length=255, verbose_name="Sinfi", choices=GROUP)
    school = models.CharField(max_length=255, verbose_name="Maktabi")
    phone_number = models.CharField(max_length=255, verbose_name="Tel. raqami")
    
    status = models.BooleanField(default=False, verbose_name="Holati")
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    
    
    
    