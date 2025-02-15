from django.shortcuts import render,redirect


from django.views.generic import *
# Create your views here.
from .forms import EventForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Person.models import Person
from .models import *
from django.urls import reverse_lazy

def listEvent(request):
    events  = Event.objects.filter(state=True)
    return render(request, 'events/list.html' , { "list" :events})



@login_required
def detailsEvent(request , ide):
    event1 = Event.objects.get(id=ide)
    
    btn= False
    
    participant = Participants.objects.filter(person=request.user, event=event1)
    
    
    print(participant)
    if participant:
        btn =True
        
    else:
        btn=False
    
    
    return render(request,'events/details.html', {"event":event1 , "button":btn })



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



class Add(LoginRequiredMixin,CreateView):
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
    
    


def deleteEvent(request,idEvent):
    
    event = Event.objects.get(id=idEvent)
    
    if event:
        event.delete()
        return redirect('list')




def participer (request ,ide):
    
    e1 = Event.objects.get(id=ide)
    
    p1 = request.user
    
    participant = Participants.objects.create(person=p1 , event=e1)
    
    if participant:
        participant.save()
        
        e1.nbr_participants+=1
        e1.save()
        return redirect("list")
    

def cancel (request ,ide):
    
    e1 = Event.objects.get(id=ide)
    
    p1 = request.user
    
    participant = Participants.objects.filter(person=p1 , event= e1)
    
    if participant:
        participant.delete()
        
        e1.nbr_participants-=1
        e1.save()
        return redirect("list")
    