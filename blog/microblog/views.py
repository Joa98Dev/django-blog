from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import BlogPost

# Create your views here.
class Index(ListView):
    model = BlogPost
    queryset = BlogPost.objects.all().order_by('-date')
    template_name = 'microblog/index.html'


    '''
    def get(self, request):
        return render(request, 'microblog/index.html')
    '''
    
    #https://youtu.be/sMqDJovFO-Y?si=2ulxWmYxLLSz2El2&t=781
