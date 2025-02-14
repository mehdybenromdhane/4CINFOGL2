

from django.urls import path

from .views import *

urlpatterns = [
    path('' ,  listEvent ,name="list"),
    
    path('details/<int:ide>', detailsEvent , name="detailsE" ),
    
    path('detailsClass/<int:pk>', Details.as_view() , name="detailsClass" ),

    path('add/', addEvent , name="addEvent" ),
    path('addClass/', Add.as_view() , name="addEventClass" ),

    
    path('update/<int:pk>', Update.as_view() , name="updateEvent" ),
    path('delete/<int:pk>',  Delete.as_view() , name="deleteEvent" ),

    path('listclass/' ,  Events.as_view())

]
