from django import forms
import datetime
from .models import Appointment

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"

class AppointmentForm(BaseForm):
    datetime = forms.DateTimeField(initial=datetime.date.today)
    description = forms.CharField(widget=forms.Textarea, label="Description")
    class Meta:
        model = Appointment
        fields = ('datetime', 'description',)
