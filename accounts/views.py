from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages

from . forms import RegistrationForm
from . models import Account

# Create your views here.

def register_seeker(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
        
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                email = email,
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password
            )
            user.phone_number = phone_number
            user.is_active = True
            user.role = 'Job Seeker'
            user.save()
            return redirect('home')
        
            
    else:
        form = RegistrationForm()
    
    context = {
        'form':form
    }

    return render(request,'register_seeker.html',context)

def register_recruiter(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
        
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                email = email,
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password
            )
            print("Form is valid")
            user.phone_number = phone_number
            user.is_active = True
            user.role = 'Job Recruiter'
            user.save()
            return redirect('home')
        else:
            print(form.errors)
            
    else:
        form = RegistrationForm()
    
    context = {
        'form':form
    }

    return render(request,'register_recruiter.html',context)


def login(request):
    if request.method == "POST":
        print("request is post")
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email, password = password)
        if user is not None:
            print("user is there")
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")

           
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')