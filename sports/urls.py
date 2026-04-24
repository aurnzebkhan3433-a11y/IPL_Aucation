"""
URL configuration for sports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vote_analysis_data import views


urlpatterns = [
    path('shopping_account/',include('shopping_account.urls')),
    path('register_shop/',include('register_shop.urls')),
    path('shop/',include('shop.urls')),
    path('graph2/',views.vote_graph2,name="vote_graph2"),
    path('graph1/',views.vote_graph1,name="vote_graph1"),
    path('graph/',views.vote_graph,name="vote_graph"),
    path('vote_count/',views.vote_count,name="vote_count"),
    path('show_results/',views.show_results,name="show_results"),
    path('vote_analysis_data/',include('vote_analysis_data.urls')),
    path('login/',include('login.urls')),
    path('dc_teams/',include('dc_teams.urls')),
    path('csk_teams/',include('csk_teams.urls')),
    path('register_auction/',include('register_auction.urls')),
    path('teams/',include('teams.urls')),
    path('',include('ipl.urls')),
    path('admin/', admin.site.urls),
]
