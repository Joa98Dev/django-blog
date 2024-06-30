from django.shortcuts import render
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    # get will handle the HTTP GET request
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    # post will handle the HTTP POST request
    def post(self, request):
        pass
