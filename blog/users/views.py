#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    # get will handle the HTTP GET request
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    # post will handle the HTTP POST request
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("ERROR\Something went wrong :(")
