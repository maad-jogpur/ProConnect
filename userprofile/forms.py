from django import forms
from . models import Profile

class SeekerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','skills','experience')
        widgets = {
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self,*args,**kwargs):
        super(SeekerProfileForm,self).__init__(*args,**kwargs)
        self.fields['profile_photo'].widget.attrs = {'Placeholder':'Upload Profile Picture','class':'form-control'}
        self.fields['skills'].widget.attrs = {'Placeholder':'Enter Skills','class':'form-control'}
        self.fields['experience'].widget.attrs = {'Placeholder':'Enter Experience','class':'form-control'}


class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','company_name','company_description')
        widgets = {
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self,*args,**kwargs):
        super(RecruiterProfileForm,self).__init__(*args,**kwargs)
        self.fields['profile_photo'].widget.attrs = {'Placeholder':'Upload Profile Picture','class':'form-control'}
        self.fields['company_name'].widget.attrs = {'Placeholder':'Enter Company Name','class':'form-control'}
        self.fields['company_description'].widget.attrs = {'Placeholder':'Enter Company Description','class':'form-control'}