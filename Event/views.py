from django.shortcuts import render


from django.views.generic import ListView
# Create your views here.


from .models import Event

def listEvent(request):
    
    
    events  = Event.objects.filter(state=True)
    
    return render(request, 'events/list.html' , { "list" :events})




class Events(ListView):
    
    model=Event
    
    template_name="events/list.html"
    context_object_name="list"
