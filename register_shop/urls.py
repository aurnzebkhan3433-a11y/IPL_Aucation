from django.urls import path
from .import views

urlpatterns=[

    path('',views.reg_shop,name="reg_shop"),
    path('reg_shop_datasave/',views.reg_shop_datasave,name="reg_shop_datasave"),
    path('datalogins/',views.datalogins,name="datalogins"),
    
]