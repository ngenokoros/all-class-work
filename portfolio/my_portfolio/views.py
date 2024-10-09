from msilib import add_data
from tkinter import image_names

from django.db.models.fields import return_None
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
 return render(request, 'about.html')


def services(request):
 return render(request, 'services.html')

def add(request):
 return render(request,'add-data.html')
 def insert_data(request):
     if request.method == "POST":
         name=request.POST('name')
         email=request.POST('email')
         age=request.POST('age')
         image=request.POST('image')



     return render(request,'add-data.html')