from django import forms
from .models import DisasterName


class FormDisasterName(forms.ModelForm):
    class Meta:
        model = DisasterName
        fields = '__all__'
