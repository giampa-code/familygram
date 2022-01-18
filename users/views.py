"""Users views"""
# Django

from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# forms
from users.forms import ProfileForm, SignUpForm

# Create your views here.
def login_view(request):
    """Login view"""
    #if the user is already logged
    if request.user.is_authenticated:
        return redirect('posts:feed')


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error':'Invalid username or password'})


    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """User logout view"""
    logout(request)
    # Redirect to a success page.
    return redirect('users:login')


def signup_view(request):
    """User signup view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('users:login')
    else:
        form = SignUpForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form':form,
        }
    )


@login_required
def update_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:update')
        else:
            form = ProfileForm(request.POST, request.FILES)


    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name = 'users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )