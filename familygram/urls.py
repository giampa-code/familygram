"""familygram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static # para ver fotos

# Views
from familygram import views as local_views



urlpatterns = [
    # home
    path('', local_views.home, name='home'),
    
    # admin
    path('admin/', admin.site.urls, name='admin'),
    
    # Posts
    path('',include(('posts.urls', 'posts'),namespace='posts')),
    
    # Users
    path('users/',include(('users.urls', 'users'),namespace='users') ),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #truco para mostrar las imagenes
