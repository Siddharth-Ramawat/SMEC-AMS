from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ProfileRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            try:
                user = form.save()
                userprofile = Profile.objects.get(user=user)
                userprofile.dept=profile_form.cleaned_data['dept']
                userprofile.registration_number=profile_form.cleaned_data['registration_number'].upper()
                userprofile.job_role=profile_form.cleaned_data['job_role']
                userprofile.work_location=profile_form.cleaned_data['work_location']
                userprofile.company=profile_form.cleaned_data['company']
                userprofile.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                messages.success(request, f'Your account has been created successfully')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('dash-home')
            except Exception as e:
                print(e)
                messages.warning(request, f'There was some issue')
                return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def view_profile(request, *args, **kwargs):
    if request.method == 'GET':
        #profile_user = Profile.objects.get(id=kwargs['id'])
        user = User.objects.get(id = kwargs['id'])
        profile_user = Profile.objects.get(user_id = user.id)
        return render(request, 'users/view_profile.html', context={'view_user': profile_user, 'title': 'User Profile'})

    return render(request, 'users/view_profile.html', context={'title': 'User Profile'})


@login_required
def update_password(request, *args, **kwargs):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'Password updated successfully')
            return HttpResponseRedirect('logout')
        else:
            messages.warning(request, f"Passwords doesn't pass the required criteria or doesn't match.Please check")
            return render(request, template_name='users/profile.html')
    else:
        password_form = PasswordChangeForm(request.user)
        context = {
            'password_form': password_form,
            'title': 'Change Password'
        }
    return render(request, 'users/profile.html', context=context)
