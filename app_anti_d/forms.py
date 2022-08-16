from django import forms
from .models import DisasterName, HearingReportsFromLocalGovernment


class FormDisasterName(forms.ModelForm):
    class Meta:
        model = DisasterName
        fields = '__all__'


class FormHearingReportsFromLocalGovernment(forms.ModelForm):
    class Meta:
        model = HearingReportsFromLocalGovernment
        fields = '__all__'
        widgets = {
            "reported_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "updated_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
