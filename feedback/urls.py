from django.urls import path

from .views import FeedbackView

urlpatterns =[
    path('feedback/',FeedbackView,template="form_template.html")

]