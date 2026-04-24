from django.urls import path
from .import views
urlpatterns=[
    
    path('register_auction/',views.reg_auction,name='myregister'),
    path('',views.reg,name='register')
]