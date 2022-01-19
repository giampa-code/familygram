"""Users views"""
# Django

from multiprocessing import context
from django.contrib.auth import authenticate, login, logout, views as auth_views
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


# Login Class View
class LoginView(auth_views.LoginView):
    """Login view with classes"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


# Logout class view
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view with classes"""
    pass


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
        #import pdb; pdb.set_trace()
        return context
