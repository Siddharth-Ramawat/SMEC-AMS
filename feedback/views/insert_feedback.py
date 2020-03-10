from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from ..forms import FeedbackForm


class FeedbackView(View):
    form_class = FeedbackForm
    def get(self,request,*args,**kwargs):
        return render(request,
                      template_name='insert_feedback.html',
                      context={'form':self.form_class})

    def post(self,request,*args,**kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")

        return render(request,'insert_feedback.html',{'form':self.form_class})


