from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Register_shop


def reg_shop(request):
    return render(request,'register_shop_page.html')

# Create your views here.
def reg_shop_datasave(request):
    if request.method=='POST':
        names=request.POST['names']
        numbers=request.POST['numbers']
        emails=request.POST['emails']
        passwords=request.POST['passwords']

        db=Register_shop(names=names,numbers=numbers,emails=emails,passwords=passwords)
        db.save()
        return render(request,'shop_login_page.html',{})
    

def datalogins(request):
    if request.method=='POST':
         
         numbers=str(request.POST['numbers'])   
         passwords=str(request.POST['passwords'])
         
        
         
         count=0
    db=Register_shop.objects.all().values()
    for x in db:
     
     
     if (str(x['numbers'])==numbers and str(x['passwords'])==passwords):
       
       count=count+1
    
    if count>0:
        #return HttpResponse("Login Succsessfully")
        return render(request,'shopping_page.html',{})
    else:
        return HttpResponse("Login Failed") 