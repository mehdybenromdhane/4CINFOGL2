from django.shortcuts import render,redirect

# Create your views here.
from .forms import UserRegisterForm

from django.contrib.auth import login,authenticate
def register(request):
    
    form = UserRegisterForm()
    
    if request.method =="POST":
        
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            user =form.save()
            
            login(request,user)
            
            redirect("list") 
    
    
    return render(request , 'person/register.html' , {"form":form})


def login_user (request):
    
    
    if (request.method=="POST"):
         name = request.POST['user']
         
         pwd = request.POST['password']
         
         user = authenticate(request , username=name ,password=pwd)
         
         if user:
             login(request,user)
             return redirect("list")
         else:
            return redirect('login')
         
    
    
    return render(request,'person/login.html',{})