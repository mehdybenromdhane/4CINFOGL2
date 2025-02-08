

from django.urls import path

from .views import listEvent, Events

urlpatterns = [
    path('list/' ,  listEvent),
        path('listclass/' ,  Events.as_view())

]
