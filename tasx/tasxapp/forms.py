from django import forms
from .models import *

class ReportForm(forms.ModelForm):

        class Meta:
            model = Report
            fields = ('title', 'status', 'descr', 'category',)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
