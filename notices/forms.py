from django import forms
from .models import Notice


class CreateNoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ('title', 'short_description', 'long_description', 'duration',
                  'pref_date', 'event_location_postcode')

