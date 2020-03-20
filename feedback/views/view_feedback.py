from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Feedback
from django.contrib.auth.decorators import login_required


# @login_required
class ViewAllFeedback(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        if kwargs:
            feedback_entries = Feedback.objects.filter(category=kwargs['cat'])
            return render(request, template_name="view_feedback.html", context={'feedback': feedback_entries, 'title':'View Feedback'})

        feedback_entries = Feedback.objects.all()
        return render(request, template_name="view_feedback.html", context={'feedback': feedback_entries, 'title':'View Feedback'})

