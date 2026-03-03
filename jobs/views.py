from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404

from . models import Job
from userprofile.models import Profile
from applications.models import Application
# Create your views here.

def jobs(request):

    unique_locations = Job.objects.values_list('job_location', flat=True).distinct()
    unique_companies = Profile.objects.values_list('company_name',flat=True).distinct()


    jobs = Job.objects.all()
    location_query = request.GET.get('location')
    query = request.GET.get('search')
    company = request.GET.get('company')
    sortby_query = request.GET.get('sortby')
 
    if location_query:
        jobs = jobs.filter(job_location=location_query)


    if query:
        jobs = jobs.filter(Q(title__icontains = query)|Q(description__icontains = query)|Q(requirement__icontains = query)).distinct()
 

    if company:
        jobs = jobs.filter(account__profile__company_name = company)
    
    if sortby_query == "oldest":
        jobs = jobs.order_by('created_at')
    elif sortby_query == "recent":
        jobs = jobs.order_by('-created_at')
    elif sortby_query == "A-Z":
        jobs = jobs.order_by('title')
    elif sortby_query == "Z-A":
        jobs = jobs.order_by('-title')
   


    context = {
        'jobs': jobs,
        'unique_locations': unique_locations,
        'unique_companies': unique_companies,
        'query':query
    }
    return render(request, 'jobs.html', context)



def job_detail(request,pk):
    try:
        job = Job.objects.get(id=pk)
        
    except:
        job=None
    
    context = {
        'job':job,
        
    }
    return render(request,'job_detail.html',context)

@login_required(login_url="login")
def apply_job(request,pk):
    job = Job.objects.get(pk=pk)
    if request.method == "POST":
        user = request.user
        resume = request.FILES['resume']
        cover_letter = request.POST['cover_letter']

        application = Application.objects.create(
            job = job,
            user = user,
            resume = resume,
            cover_letter = cover_letter
        )

        application.save()
        return redirect('home')

    context = {
        'job':job
    }
    return render(request,'apply_job.html',context)