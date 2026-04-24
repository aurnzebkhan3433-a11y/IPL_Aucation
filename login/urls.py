from django.urls import path
from .import views
urlpatterns=[

path('',views.log,name='login'),
path('check/',views.datalogin,name='login_check')
]
