from django import forms
from .models import DisasterName, HearingReports


class FormDisasterName(forms.ModelForm):
    class Meta:
        model = DisasterName
        fields = '__all__'


class FormHearingReports(forms.ModelForm):
    class Meta:
        model = HearingReports
        fields = '__all__'
        widgets = {
            "reported_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "updated_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
