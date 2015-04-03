from django.http import HttpResponse
from django.views.generic.edit import CreateView
from models import Users
from django import forms
import datetime
from django.db.models.fields import DateField
import json


class EditForm(forms.Form):
    class Meta:
        model = Users

class AjaxableResponseMixin(object):

    def render_to_response(self, context, **httpresponse_kwargs):
        return self.get_json_response(
            self.convert_context_to_json(context),
            **httpresponse_kwargs
        )

    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(
            content,
            content_type='application/json',
            **httpresponse_kwargs
        )
    def convert_context_to_json(self, context):
        u""" This method serialises a Django form and
        returns JSON object with its fields and errors
        """
        form = context.get('form')
        to_json = {}
        options = context.get('options', {})
        to_json.update(options=options)
        to_json.update(success=context.get('success', False))
        fields = {}
        for field_name, field in form.fields.items():
            if isinstance(field, DateField) \
                    and isinstance(form[field_name].value(), datetime.date):
                fields[field_name] = \
                    unicode(form[field_name].value().strftime('%d.%m.%Y'))
            else:
                fields[field_name] = \
                    form[field_name].value() \
                    and unicode(form[field_name].value()) \
                    or form[field_name].value()
        to_json.update(fields=fields)
        if form.errors:
            errors = {
                'non_field_errors': form.non_field_errors(),
            }
            fields = {}
            for field_name, text in form.errors.items():
                fields[field_name] = text
            errors.update(fields=fields)
            to_json.update(errors=errors)
        return json.dumps(to_json)


class UserChangeForm(AjaxableResponseMixin, CreateView):
    model = Users
    form_class = EditForm