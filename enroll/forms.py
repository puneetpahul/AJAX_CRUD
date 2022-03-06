from .models import User
from django import forms

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'})
        }