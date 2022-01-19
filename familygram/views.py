"""familygram views"""

# Django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def home(request):
    """If user is valid, go to feed. Else, login"""
    return redirect('posts:feed')

