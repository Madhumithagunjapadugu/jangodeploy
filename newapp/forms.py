from newapp.models import employee
from django import forms
class emp_form(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
