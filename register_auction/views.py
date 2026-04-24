from django.shortcuts import render ,redirect
from register_auction.models import Datasave
from django.http import HttpResponse 
def reg(request):
    return render(request,'register.html',{})

# Create your views here.
def reg_auction(request):
    if request.method=='POST':
        name=request.POST['names']
        phonenumber=request.POST['phones']
        email=request.POST['emails']
        state=request.POST['states']
        password=request.POST['passwords']
        x=Datasave(name=name,phonenumber=phonenumber,email=email,state=state,password=password)
        x.save()
        
        return redirect("/")
    
       

