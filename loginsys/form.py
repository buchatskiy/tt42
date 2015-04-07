# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, label=("E-mail*"))
    first_name = forms.CharField(required = False, label=("First name"))
    last_name = forms.CharField(required = False, label=("Last name"))
    username = forms.CharField(required = True, label=("Login*"), help_text=('No more than 30 characters. Only letters, numbers and symbols @/./+/-/_.'))
    password1 = forms.CharField(required = True, label=("Password*:"), widget=forms.PasswordInput)
    password2 = forms.CharField(required = True, label=("Password confirm*:"), help_text=('Enter the same password as above, for confirmation.'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 4:
            raise forms.ValidationError('The password must be at least 4 characters')
        return password


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('User with this e-mail already exists, login please.')
        return email