from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.views import View

from django.shortcuts import render

from ..forms import FeedbackForm


class FeedbackView(View):
    form_class = FeedbackForm
    template_name = "form_template.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request,self.template_name,{'form':self.form_class})


