from django.forms import models
from django import forms
from django.contrib.auth.models import User

class UserForm(models.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__()
        self.fields['username'].widget.attrs.update({
            'placeholder':'UserName',
            'class':'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder':'Password',
            'class':'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder':'Email ID',
            'class':'form-control'
        })