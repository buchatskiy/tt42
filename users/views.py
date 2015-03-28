from django.shortcuts import render_to_response
from users.models import Users


def main(request, htmlfile):
    first_user = Users.objects.all()[0]
    args = {'first_name': first_user.first_name,
            'last_name': first_user.last_name,
            'date_birth': first_user.date_birth,
            'email': first_user.email,
            'jabber': first_user.jabber,
            'skype': first_user.skype,
            'bio': first_user.bio,
            'other_contacts': first_user.other_contacts,
            }
    return render_to_response(htmlfile, args)
