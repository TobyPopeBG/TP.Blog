from django.shortcuts import render
from django.views import generic
from .models import Post, About

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutDetail(generic.DetailView):
    model = About
    slug_field = 'about_slug'
    template_name = 'about_detail.html'