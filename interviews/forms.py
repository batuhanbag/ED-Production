from django import forms
from .models import Interviews


class NewsForm(forms.ModelForm):
    class Meta:
        model = Interviews
        fields = ["title", "content", "interviews_image"]
