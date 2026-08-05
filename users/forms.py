from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CitizenRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text="Choose a unique username."
    )

    class Meta:

        model = User

        fields = (
            "username",
            "full_name",
            "email",
            "mobile_number",
            "password1",
            "password2",
        )

    def save(self, commit=True):

        user = super().save(commit=False)

        user.role = User.Role.CITIZEN

        if commit:
            user.save()

        return user