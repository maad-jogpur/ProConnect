from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from . forms import PostJobForm,EditJobForm
from jobs.models import Job
from applications.models import Application
from userprofile.models import Profile

# Create your views here.


def recruiter_dashboard(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    jobs = Job.objects.filter(account = user).annotate(
        count = Count('application')
    )
    
    context = {
        'jobs':jobs,
        'profile':profile
    }
    return render(request,'recruiter_dashboard.html',context)

def post_job(request):
    if request.method == "POST":
        form = PostJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.account = request.user
            job.save()
            return redirect('recruiter_dashboard')

    else:        
        form = PostJobForm()
      
    context = {
        'form':form,

    }
    return render(request,'post_job.html',context)

def edit_job(request,pk):
    job = Job.objects.get(pk=pk)
    if request.method == "POST":
        form = EditJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('recruiter_dashboard')
    else:
        form = EditJobForm(instance=job)
    context = {
        'job':job,
        'form':form
    }
    return render (request,'edit_job.html',context)

def delete_job(request,pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    return redirect( 'recruiter_dashboard')

def seeker_dashboard(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    applications = Application.objects.filter(user=user)
    context = {
        'applications':applications,
        'profile':profile
    }
    return render(request,'seeker_dashboard.html',context)


def view_applicants(request,pk):
    job = get_object_or_404(Job,pk=pk,account=request.user)
    applications = Application.objects.filter(job=job)
    count = Application.objects.filter(job=job).count()
    context = {
        'applications':applications,
        'job':job,
        'count':count
    }

    return render(request,'view_applicants.html',context)

def select_applicant(request,pk):
    application= Application.objects.get(pk=pk)
    application.status = "Selected"
    application.save()
    user = application.user
    current_site = get_current_site(request)
    subject = "You are selected"
    message = render_to_string('select_email.html',{
        'user':request.user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'token':default_token_generator.make_token(user),
        'application':application,
    })
    to_email = user.email
    send_email = EmailMessage(subject,message,to=[to_email])
    send_email.content_subtype = "html"
    send_email.send()
    return redirect("view_applicants", pk=application.job.id)

def reject_applicant(request,pk):
    application= Application.objects.get(pk=pk)
    application.status = "Rejected"
    application.save()
    user = application.user
    current_site = get_current_site(request)
    subject = "Please verify your account"
    message = render_to_string('reject_email.html',{
        'user':request.user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'token':default_token_generator.make_token(user),
        'application':application,
    })
    to_email = user.email
    send_email = EmailMessage(subject,message,to=[to_email])
    send_email.content_subtype = "html"
    send_email.send()
    return redirect("view_applicants", pk=application.job.id)