"""Users views"""
# Django

from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post

# forms
from users.forms import  SignUpForm
from users.models import Profile

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


class SignUpView(FormView):
    """Users signup view with Class Views"""
    template_name ='users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

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


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view with Class Views."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    
    def get_object(self):
        """Returns users profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to users profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

# Vista detallada para el usuario
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""
    template_name = 'users/detail.html'
    # QuerySet
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    # sobre escribiendo una función

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
