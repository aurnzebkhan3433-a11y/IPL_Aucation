from django.urls import path
from .import views

urlpatterns=[
    path('',views.dc,name='dc'),
]