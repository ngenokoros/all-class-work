
from django.shortcuts import render

from .models import Student


def add(request):
    return render(request, 'add.html')

def view(request):
    students = Student.objects.all()
    return render(request,'view-data.html',{'students':students})


# Create your views here.
def insert_data(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        adm_no = request.POST.get('adm_no')
        image = request.POST.get('image')

        student= Student(name=name, age=age, email=email, adm_no=adm_no, image=image)
        student.save()

    return render(request,'add.html')