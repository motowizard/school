from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Dept,Course,Members

# Create your views here.
def home(request):
    dept=Dept.objects.all()
    return render(request,'index.html',{'dept':dept})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('add_purpose')
        else:
            messages.info(request, "Authentication incorrect")
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('register')
    return render(request, 'register.html')



def newform(request):
    departments=Dept.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name','')
        dob = request.POST.get('dob','')
        age = request.POST.get('age','')
        gender = request.POST.get('gender','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        purpose = request.POST.get('purpose','')
        members=Members(name=name,dob=dob,age=age,gender=gender,purpose=purpose,phone=phone,email=email,address=address)
        members.save()
        return redirect('message')

    return render(request,'newform.html',{'departments':departments})


def logout(request):
    auth.logout(request)
    return redirect('/')
def add_purpose(request):
    return render(request,'add_purpose.html')

def message(request):
    return render(request,'message.html')

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id)
    return render(request, 'load_course.html', {'courses': courses})
