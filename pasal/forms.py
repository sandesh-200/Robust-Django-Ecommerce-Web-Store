from django import forms
from .models import Contact,Profile
from django .contrib.auth.models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    middle_name = forms.CharField(label="Middle Name", max_length=100,required=False)
    last_name = forms.CharField(label="Last Name", max_length=100,required=False)
    user_name= forms.CharField(required=True, label = "Username")
    your_email = forms.EmailField(required=True,label="Email")
    your_password = forms.CharField(label="Password",widget=forms.PasswordInput(), required=True)
    your_password_confirm = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(),required=True)
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class ProfieForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')

        


