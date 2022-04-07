from django.shortcuts import render
from django.shortcuts import HttpResponse


#views

def index(request):
    return render(request,'portfolio.html')
  