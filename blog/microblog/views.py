from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'microblog/index.html')
    
    '''https://youtu.be/sMqDJovFO-Y?si=2ulxWmYxLLSz2El2&t=781'''
