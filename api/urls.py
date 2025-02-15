
from django.urls import path


from .views import getEvents

urlpatterns = [
    path('getEvents/',getEvents )
]
