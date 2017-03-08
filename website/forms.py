from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User , Complain


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)


class UserSignUpForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.password = self.cleaned_data['password1']
        user.username = user.email
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = {'name', 'password1', 'password2', 'email'}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))


class ComplainForm(forms.ModelForm):
    def save(self, request , commit=True):
        complain = super(ComplainForm, self).save(commit=False)
        complain.name = self.cleaned_data['name']
        complain.category = self.cleaned_data['category']
        complain.description = self.cleaned_data['description']
        complain.area = self.cleaned_data['area']
        complain.user = request.user
        if commit:
            complain.save()
        return complain


    class Meta:
        model = Complain
        fields = {'name' , 'description' , 'category' , 'area' }
    
