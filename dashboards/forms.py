from django import forms
from django.forms import inlineformset_factory
from jobs.models import Job


class PostJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','description','requirement','job_location','job_salary')

    def __init__(self,*agrs,**kwargs):
        super(PostJobForm,self).__init__(*agrs,**kwargs)
        self.fields['title'].widget.attrs={'Placeholder':'Title','class':'form-control mb-2'}
        self.fields['description'].widget.attrs={'Placeholder':'Description','class':'form-control mb-2'}
        self.fields['requirement'].widget.attrs={'Placeholder':'Requirement','class':'form-control mb-2'}
        self.fields['job_location'].widget.attrs={'Placeholder':'Location','class':'form-control mb-2'}
        self.fields['job_salary'].widget.attrs={'Placeholder':'Salary in LPA','class':'form-control mb-2'}

class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','description','requirement','job_location','job_salary')

    def __init__(self,*agrs,**kwargs):
        super(EditJobForm,self).__init__(*agrs,**kwargs)
        self.fields['title'].widget.attrs={'Placeholder':'Title','class':'form-control mb-2'}
        self.fields['description'].widget.attrs={'Placeholder':'Description','class':'form-control mb-2'}
        self.fields['requirement'].widget.attrs={'Placeholder':'Requirement','class':'form-control mb-2'}
        self.fields['job_location'].widget.attrs={'Placeholder':'Location','class':'form-control mb-2'}
        self.fields['job_salary'].widget.attrs={'Placeholder':'Salary in LPA','class':'form-control mb-2'}

