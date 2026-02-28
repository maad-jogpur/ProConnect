from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .forms import SeekerProfileForm,RecruiterProfileForm
from accounts.models import Account
from userprofile.models import Profile
# Create your views here.


@login_required(login_url='login')
def edit_profile_seeker(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        form = SeekerProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('edit_profile')
    else:
        form = SeekerProfileForm(instance=profile)

    context = {
        'seeker_form':form,
        'profile':profile
    }

    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def edit_profile_recruiter(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        form = RecruiterProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('edit_profile')
    else:
        form = RecruiterProfileForm(instance=profile)

    context = {
        'recruiter_form':form,
        'profile':profile
    }

    return render(request,'edit_profile.html',context)