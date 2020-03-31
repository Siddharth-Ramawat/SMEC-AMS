from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import *

class ViewAllFeedback(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            if kwargs:
                feedback_entries = Feedback.objects.filter(category=kwargs['cat'])
                return render(request, template_name="view_feedback.html", context={'feedback': feedback_entries, 'title': 'View Feedback'})

            feedback_entries = Feedback.objects.all()
            return render(request, template_name="view_feedback.html", context={'feedback': feedback_entries, 'title': 'View Feedback'})

        return render(request, template_name="dash/stalker.html", context={'title': 'Alert'} )

class ClearFeedbackView(LoginRequiredMixin, View):
    model = Feedback
    form_class = ClearFeedback
    template_name = "clear_feedback_form.html"

    def get(self,request,*args,**kwargs):
        return render(request,template_name="clear_feedback_form.html",context={'form':form_class})

    def form_valid(self,form):
        delete_ = Feedback.objects.all()
        return HttpResponse(render_to_string('success.html'))
