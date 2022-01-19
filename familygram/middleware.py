"""familygram middleware catalog"""
# Django
from django.shortcuts import redirect
from django.urls import reverse

# Utilities
from django.contrib import messages

class ProfileCompletionMiddleware:
    """
    Profile completion middleware
    Ensure every user that is using the platform
    have their profile picture and bio
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_anonymous:
            # get profile objetc
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.biography or not profile.picture:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        messages.error(request, 'Debes tener una biografía y una imagen para poder usar la app.')
                        return redirect('users:update')


        response = self.get_response(request)

        return response

class NotStaffMiddleware:
    """
    This middleware ensure that only staff members
    can add new photos to the page
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path in [reverse('posts:create')]:
            if not request.user.is_staff:
                profile = request.user.profile
                messages.error(request, 'Solo miembros del staff pueden añadir fotos.')
                return redirect('posts:feed')


        response = self.get_response(request)

        return response