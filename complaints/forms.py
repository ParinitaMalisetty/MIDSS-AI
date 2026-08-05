from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            "title",
            "description",
            "category",
            "image",
            "latitude",
            "longitude",
        ]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "latitude": forms.NumberInput(attrs={
                "class": "form-control",
                "readonly": True
            }),

            "longitude": forms.NumberInput(attrs={
                "class": "form-control",
                "readonly": True
            }),

        }