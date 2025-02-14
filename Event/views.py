from django.shortcuts import render,redirect


from django.views.generic import *
# Create your views here.
from .forms import EventForm

from .models import Event
from django.urls import reverse_lazy

def listEvent(request):
    events  = Event.objects.filter(state=True)
    return render(request, 'events/list.html' , { "list" :events})




def detailsEvent(request , ide):
    event = Event.objects.get(id=ide)
    return render(request,'events/details.html', {"event":event })



class Details(DetailView):
    model= Event
    template_name="events/details.html"
    context_object_name ="event"



class Events(ListView):
    
    model=Event
    
    template_name="events/list.html"
    context_object_name="list"


      
      

def addEvent(request):
    
    form = EventForm()
      
    if request.method == "POST":
        
        form = EventForm(request.POST , request.FILES)
        form.save() 
      
        return redirect("list")
    
    return render (request, "events/add.html", {"form":form})



class Add(CreateView):
    model=Event
    template_name="events/add.html"
    form_class= EventForm
    
    
    

class Update(UpdateView):
    model=Event
    template_name="events/update.html"
    form_class=EventForm
    
    success_url= reverse_lazy("list")
    
    
    
    
class Delete(DeleteView):
    model=Event
    success_url= reverse_lazy("list")
    
    template_name="events/delete.html"
