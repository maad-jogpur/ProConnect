from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django import forms



from . forms import RegistrationForm
from . models import Account
from userprofile.models import Profile

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
            user.role = 'Job Seeker'
            user.save()

            current_site = get_current_site(request)
            subject = "Please verify your account"
            message = render_to_string('seeker_account_verification.html',{
                'user':request.user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user)
            })
            to_email = user.email
            send_email = EmailMessage(subject,message,to=[to_email])
            send_email.content_subtype = "html"
            send_email.send()
            messages.info(request,"Please verify your email address")
            return redirect('register_seeker')
        
            
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
            user.role = 'Job Recruiter'
            user.save()
            current_site = get_current_site(request)
            subject = "Please verify your account"
            message = render_to_string('recruiter_account_verification.html',{
                'user':request.user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user)
            })
            to_email = user.email
            send_email = EmailMessage(subject,message,to=[to_email])
            send_email.content_subtype = "html"
            send_email.send()
            messages.info(request,"Please verify your email address")
            
            
            return redirect('register_recruiter')
        else:
            print(form.errors)
            
    else:
        form = RegistrationForm()
    
    context = {
        'form':form
    }

    return render(request,'register_recruiter.html',context)

def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)
    except:
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        messages.success(request,"Verification Successful")
        user.is_active = True
        user.save()
        profile = Profile.objects.create(user = user)
        return redirect('login')
    else:
        messages.error(request,"Verification link has expired! Register Again")
        if user is not None:
            if user.role == "Job Seeker":
                if user.is_active == False:
                    user.delete()
                    return redirect('register_seeker')

            else:
                if user.is_active == False:
                    user.delete()
                    return redirect('register_recruiter')
        return redirect('home')

def login(request):
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,"Invalid Credentials")

           
    return render(request,'login.html')

def forget_password(request):
    
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = Account.objects.get(email=email)
        except:
            user = None
        if user is not None:
            current_site = get_current_site(request)
            subject = "Change your password"
            message = render_to_string('email_forget_password.html',{
                'domain': current_site,
                'user':user,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user)
            })
            to_email = user.email
            send_email = EmailMessage(subject,message,to=[to_email])
            send_email.content_subtype = 'html'
            send_email.send()
            messages.success(request,"Verification email sent!")
        else:
            messages.error(request,"User with this email address does not exist!")

    return render(request,'forget_password.html')

def reset_password_validate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(id = uid)
    except:
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        if request.method == "POST":
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password!=confirm_password:
                messages.error(request,"Passwords do not match!!")
                return render (request,'reset_password.html')
            else:
                user.set_password(password)
                user.save()
                messages.success(request,"Password changed successfully!!!!")
                return redirect('login')
        else:
            return render (request,'reset_password.html')
    
    else:
        messages.error(request,"Verification link expired!")
        return redirect('forget_password')

def change_password(request):
    user = request.user
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        if user.check_password(current_password):
            if new_password!=confirm_password:
                messages.error(request,"Both passwords do not match!!!")
            else:
                user.set_password(new_password)
                user.save()
                messages.success(request,"Password changed successfully")
                auth.logout(request)
                return redirect('login')
        else:
            messages.error(request,"Incorrect current password!!")
            return render(request,'change_password.html')
                
    return render(request,'change_password.html')



def logout(request):
    auth.logout(request)
    return redirect('home')