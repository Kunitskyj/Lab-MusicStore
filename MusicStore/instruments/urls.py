# instruments/urls.py
from django.urls import path
from .views import InstrumentList, InstrumentDetail

urlpatterns = [
    path('instruments/', InstrumentList.as_view(), name='instrument-list'),
    path('instruments/<int:pk>/', InstrumentDetail.as_view(), name='instrument-detail'),
]
