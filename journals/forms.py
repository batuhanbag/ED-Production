from django import forms
from .models import Journals


class JournalsForm(forms.ModelForm):
    class Meta:
        model = Journals
        fields = ["title", "content", "journals_image"]
