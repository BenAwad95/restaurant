from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Rate
class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('name', 'score', 'comment')
        # exclude = ['restaurant']

        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Name'}),
            'comment': widgets.Textarea(attrs={'cols':"30", 'rows':"5", 'placeholder':"Comment..."})
        }