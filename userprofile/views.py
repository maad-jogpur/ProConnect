from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .forms import SeekerProfileForm,RecruiterProfileForm,UserEditForm
from accounts.models import Account
from userprofile.models import Profile
# Create your views here.


@login_required(login_url='login')
def edit_profile_seeker(request):
    profile = Profile.objects.get(user=request.user)
    user = Account.objects.get(email = request.user.email)
    if request.method=="POST":
        form = SeekerProfileForm(request.POST,request.FILES,instance=profile)
        user_form = UserEditForm(request.POST,instance = user)
        if form.is_valid():
            if user_form.is_valid():
                form.save()
                user_form.save()
                return redirect('seeker_dashboard')
            else:
                return redirect('edit_profile')
        else:
            return redirect('edit_profile')
    else:
        form = SeekerProfileForm(instance=profile)
        user_form = UserEditForm(instance = user)

    context = {
        'user_form':user_form,
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
            return redirect('recruiter_dashboard')
        else:
            return redirect('edit_profile')
    else:
        form = RecruiterProfileForm(instance=profile)

    context = {
        'recruiter_form':form,
        'profile':profile
    }

    return render(request,'edit_profile.html',context)