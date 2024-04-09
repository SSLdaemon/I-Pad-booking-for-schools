from django import forms
from .models import Booking, Period

class BookingForm(forms.ModelForm):
    teacher_name = forms.CharField(max_length=200)
    periods = forms.ModelMultipleChoiceField(queryset=Period.objects.all(), widget=forms.CheckboxSelectMultiple)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    num_ipads = forms.IntegerField(min_value=1, max_value=40, widget=forms.Select(choices=[(i, i) for i in range(1, 41)]))

    class Meta:
        model = Booking
        fields = ['teacher_name', 'periods', 'date', 'num_ipads']