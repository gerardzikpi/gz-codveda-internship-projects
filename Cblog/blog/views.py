from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import BlogPostCreationForm,AnnouncementModelForm
from .models import BlogPost,Announcement

# Create your views here.


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "blog/BlogPostListView.html"

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        return obj


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "blog/BlogPostDetailView.html"


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostCreationForm
    template_name = "blog/BlogPostCreateView.html"
    success_url = reverse_lazy('blog:posts')
    login_url = reverse_lazy('bloguser:login')

    def form_valid(self, form):
        # Ensure the post is assigned to the currently logged-in user
        if self.request.user.is_authenticated:
            form.instance.written_by = self.request.user
            form.save()
        return super().form_valid(form)


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "blog/BlogPostDeleteView.html"
    success_url = "/"


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = "__all__"
    template_name = "blog/BlogPostUpdateView.html"
    context_object_name = "posts"
    success_url = reverse_lazy("blog:posts")

class AnnouncementListView(ListView):
    """ 
    Brief information about events and site management.
    Managed via django administration
    """

    model = Announcement
    template_name = "announcements/list.html"
    context_object_name = "news"
