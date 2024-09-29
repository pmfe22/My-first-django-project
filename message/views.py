from django.shortcuts import render
from django.views.generic import ListView
from .models import message
# Create your views here.

# def messageView(request):
#     return render(request , 'home.html')

class MessageView(ListView):
    model = message
    template_name= 'home.html'