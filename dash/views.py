from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from users.models import Profile
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dash/home.html', context)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'dash/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchUserView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):

        if request.GET.get('query') != '':
            search = request.GET.get('query')
            users = Profile.objects.filter(Q(user__username__icontains=search)|Q(job_role__icontains=search)|Q(work_location__icontains=search)|Q(company__icontains=search)\
                                           |Q(dept__iexact = search)|Q(registration_number__iexact=search)).order_by('-user_id__date_joined')
            context = {
                'title': 'Search User',
                'users': users,
                'query': search
            }
            return render(request,'dash/search_list.html', context)
        else:
            return render(request, 'dash/home.html', {'title':'Dash-Home'})

def about(request):
    return render(request, 'dash/about.html', { 'title' : 'About'})

