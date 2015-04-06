from django import forms
from models import Users


class EditForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput())
    class Meta:
        model = Users
        fields = ['first_name',
                  'last_name',
                  'date_birth',
                  'email',
                  'jabber',
                  'skype',
                  'bio',
                  'other_contacts'
                  ]
        widgets = {
                    'first_name': forms.TextInput(attrs={'required': True, 'placeholder': 'Your name'}),
                    'last_name': forms.TextInput(attrs={'required': True, 'placeholder': 'Your last name'}),
                    'date_birth': forms.DateInput(attrs={'required': True, 'placeholder': 'YYYY-MM-DD'})
                 }


"""
from datetime import date
from django.forms import widgets

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        years = [(year, year) for year in range(1900, 2015)]
        months = [(month, month) for month in range(1, 13)]
        days = [(day, day) for day in range(1, 32)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=int(datelist[0]), month=int(datelist[1]),
                    year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)
"""