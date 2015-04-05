from django import forms
from models import Users


class EditForm(forms.ModelForm):
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
