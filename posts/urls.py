"""Posts URLs."""

# Django
from django.urls import path


# Views
from posts import views as posts_views


urlpatterns = [
    
    path(route='feed',view=posts_views.PostsFeedView.as_view(), name='feed'),
    path(route='posts/new',view=posts_views.create_post, name='create'),
    path(route='posts/<int:post_id>',view=posts_views.PostView.as_view(), name='detail'),
    # lo mismo de arriba pero con funcs
    path(route='<int:post_id>', view=posts_views.view_post, name="detail2")
]
