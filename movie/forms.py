from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class HomePageForm(forms.Form):
    email = forms.EmailField(label=False)


class CreateAccountForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este endereço de e-mail já está sendo usado.')
        
        return email
