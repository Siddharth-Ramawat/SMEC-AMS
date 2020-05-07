from django.urls import path
from .views import *

urlpatterns =[
    path(r'events/', events_creation.as_view(), name="events"),
    path(r'view_events/', view_events.as_view(), name ="view_events"),
]