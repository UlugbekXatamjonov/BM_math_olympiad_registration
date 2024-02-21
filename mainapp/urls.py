from django.urls import path, include
from rest_framework import routers

from .views import Category_Vacancy_APIViewset, Statistics_APIViewset

router = routers.DefaultRouter()
router.register(r'contact', Category_Vacancy_APIViewset, basename='contact')
router.register(r'statistics', Statistics_APIViewset, basename='statistics')

urlpatterns = [
    path('', include(router.urls)),
]


