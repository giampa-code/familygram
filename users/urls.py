"""Users URLs"""

# Django
from django.urls import path

# Views
from users import views as users_views
#from django.views.generic import TemplateView

urlpatterns = [
    path(route='profile/<str:username>/', view=users_views.UserDetailView.as_view(), name='detail' ),
    path(route='login', view=users_views.login_view, name='login'),
    path(route='logout', view=users_views.logout_view, name='logout'),
    path(route='signup', view=users_views.signup_view, name='signup'),
    # Using middlewares
    path(route='profile', view=users_views.update_view, name='update'),
]
