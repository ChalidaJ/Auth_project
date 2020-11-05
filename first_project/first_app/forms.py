from django import forms
from django.core import validators
from django.forms import ModelForm
from first_app.models import Register

class Registerform(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'



#class Registration(forms.Form):
    #name = forms.CharField(max_length=20)
    #email = forms.CharField(max_length=30)
    #text = forms.CharField(widget=forms.Textarea)


