from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.
class Index(ListView):
    model = BlogPost
    queryset = BlogPost.objects.all().order_by('-date')
    template_name = 'microblog/index.html'
    paginate_by = 1


class DetailPostView(DetailView):
    model = BlogPost
    template_name = 'microblog/post.html'
