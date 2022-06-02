from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greet(request): 
    return render(request,'tunde/index.html')



def about(request):
    return render(request,'tunde/about.html')