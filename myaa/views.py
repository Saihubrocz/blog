from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def desktop(request):
    all_emps = Employee.objects.all()
    context = {
        'all_emps' : all_emps,
    }
    return render(request,'myapp/desktop.html',context)

def home(request):
    return render(request,'myapp/home.html')


def about(request):



    return render(request,'myapp/about.html')

def services(request):
    return render(request,'myapp/services.html')

def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        add_emp = Employee(firstname=firstname, lastname=lastname,
         email=email, password=password, confirmpassword=confirmpassword)
        add_emp.save()
        return HttpResponse("thank you")
    return render(request,'myapp/contact.html')
