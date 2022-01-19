"""Post views"""
# Django
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy


# Forms
from posts.forms import PostForm

# Models
from posts.models import Post



class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 6
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post with class views"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

@login_required
def create_post(request):
    """Create a new post with functions views"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )


# Vista post usando funcs
@login_required
def view_post(request, post_id='post_id'):
    """View a post"""
    post = Post.objects.get(id=post_id)
    #import pdb; pdb.set_trace()

    return render(request, template_name='posts/post.html', context={'post':post})
    

# Vista detallada para el usuario usando ClassViews
class PostView(LoginRequiredMixin, DetailView):
    """Post detail view"""
    template_name = 'posts/post.html'
    # QuerySet
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
