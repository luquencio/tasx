from django import forms
from .models import *

class ReportForm(forms.ModelForm):

        class Meta:
            model = Report
            fields = ('title', 'status', 'descr', 'category',)
