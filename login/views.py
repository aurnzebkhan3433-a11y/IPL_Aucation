from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from register_auction.models import Datasave
from .models import Login
def log(request):
    return render(request,'login_form.html',{})

# Create your views here.
def datalogin(request):
    if request.method=='POST':
         
         phone_number=str(request.POST['numbers'])
         password=str(request.POST['passwords'])
         
        
         
         count=0
    db=Datasave.objects.all().values()
    for x in db:
     
     
     if (str(x['phonenumber'])==phone_number and str(x['password'])==password):
       
       count=count+1
    
    if count>0:
        #return HttpResponse("Login Succsessfully")
        return render(request,'auction_login_page.html',{})
    else:
        return HttpResponse("Login Failed")

   # context={
   #     'msg':"YES"
   # }
   # return HttpResponse(template.render(context,request))