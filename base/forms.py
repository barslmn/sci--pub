from django import forms
from captcha.fields import CaptchaField


class AllauthSignupForm(forms.Form):

    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    captcha = CaptchaField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
