from django import forms
from .models import *

class ReportForm(forms.ModelForm):

        class Meta():
            model = Report
            fields = ('title', 'descr', 'category','photo', 'schedule', )


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), min_length=8)
