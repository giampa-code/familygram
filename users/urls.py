"""Users URLs"""

# Django
from django.urls import path

# Views
from users import views as users_views

urlpatterns = [
    path(route='login', view=users_views.login_view, name='login'),
    path(route='logout', view=users_views.logout_view, name='logout'),
    path(route='signup', view=users_views.SignUpView.as_view(), name='signup'),
    # Using middlewares
    path(route='profile', view=users_views.UpdateProfileView.as_view(), name='update'),
    path(route='profile/<str:username>/', view=users_views.UserDetailView.as_view(), name='detail' ),
]
