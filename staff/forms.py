from django import forms
from Sparky.models import *



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user','treatment','dentist','date','time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.TimeInput(attrs={'type': 'time'}),
        }

class AppointmentStatus(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user','treatment','dentist','date','time_slot','status']
        widgets = {
        }

class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = ['user','workDays', 'startTime', 'endTime']
        widgets = {
            'workDays': forms.TextInput(attrs={'placeholder': 'เช่น 1,2,3 (จันทร์,อังคาร,พุธ)'}),
            'startTime': forms.TimeInput(attrs={'type': 'time'}),
            'endTime': forms.TimeInput(attrs={'type': 'time'}),
        }

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ["treatmentName","price"]

class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ["extraName","price"]