from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=4, min_length=4, label="Password (4 digit number)")

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'ID',
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password.isdigit():
            raise ValidationError("Password must be a 4 digit number.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user