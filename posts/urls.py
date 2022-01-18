"""Posts URLs."""

# Django
from django.urls import path


# Views
from posts import views as posts_views


urlpatterns = [
    
    path(route='',view=posts_views.list_posts, name='feed'),
    path(route='posts/new',view=posts_views.create_post, name='create'),
]
