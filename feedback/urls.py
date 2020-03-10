from django.urls import path

from feedback.views import *

urlpatterns =[
    path(r'feedback/',FeedbackView.as_view(),name="feedback_home")

]