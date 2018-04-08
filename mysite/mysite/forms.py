from django import forms
from django.forms.widgets import SelectDateWidget
import account.forms

class SignupForm(account.forms.SignupForm):
    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1910, 1991)))

class AppForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    phone_number = forms.CharField(label='Phone Number')
    address1 = forms.CharField(label="Address line 1", max_length=50)
    address2 = forms.CharField(label="Address line 2", max_length=50, required=False)
    zipcode = forms.CharField(label="Zipcode", max_length=50, required=False)
    city = forms.CharField(label="City", max_length=50)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female')))
    university = forms.CharField(label='University', max_length=100)
    graduating_class = forms.IntegerField(label='Graduating Class', max_value=2050)
    major = forms.CharField(label='Major', max_length=50)
    track = forms.ChoiceField(label='Track', choices=(('1', 'Track1'),('2', 'Track2'),('3', 'Track3')))
    reimbursement = forms.ChoiceField(label='Travel Reimbursement', choices=(('1', 'No'),('2', 'Yes')))
    contingency = forms.ChoiceField(label='Contingency', choices=(('1', 'No'),('2', 'Yes')))
    team = forms.ChoiceField(label='Team', choices=(('1', 'No'),('2', 'Yes')))
    resume = forms.FileField(label='Resume')
