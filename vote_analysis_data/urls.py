from django.urls import path
from .import views

urlpatterns=[
    
    path('',views.Anal_data,name="Anal_data"),
]