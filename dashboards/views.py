from django.shortcuts import render,redirect
from django.db.models import Count
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
    job = Job.objects.get(pk=pk)
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
    return redirect("view_applicants", pk=application.job.id)

def reject_applicant(request,pk):
    application= Application.objects.get(pk=pk)
    application.status = "Rejected"
    application.save()
    return redirect("view_applicants", pk=application.job.id)