from django import forms
from . models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder':'Enter password','class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder':'Enter confirm password','class':'form-control'}))
    class Meta:
        model = Account
        fields = ('email','first_name','last_name','phone_number','password')

    def clean(self):
        cleaned_data =  super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError ("Passwords do not match!")

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs = {'Placeholder':'example@gmail.com','class':'form-control'}
        self.fields['first_name'].widget.attrs = {'Placeholder':'Name','class':'form-control'}
        self.fields['last_name'].widget.attrs = {'Placeholder':'Doe','class':'form-control'}
        self.fields['phone_number'].widget.attrs = {'Placeholder':'123456789','class':'form-control'}


    