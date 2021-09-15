# from django.contrib.auth import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from library.forms import SignUpForm,LoginForm
from library.models import Books
# Create your views here.

def index(request):
    return render(request, 'library/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'library/register.html',{"form":form , "msg": msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_student:
                login(request,user)
                return redirect('student')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'library/login.html',{"form":form , "msg": msg})

def admin(request):
    book_items = Books.objects.all()
    context = {"book_items":book_items}
    return render(request,'library/adminpage.html',context)

def student(request):
    return render(request,'library/student.html')

def addbooks(request):
    return render(request,'library/addnewbook.html')