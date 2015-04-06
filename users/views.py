from django.shortcuts import render_to_response, redirect
from users.models import Users
from forms import EditForm
from django.core.context_processors import csrf
from django.http import JsonResponse


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


def edit_page(request, htmlfile):
    args = {}
    args.update(csrf(request))
    first_user = Users.objects.all()[0]
    args['form'] = EditForm(instance=first_user)
    return render_to_response(htmlfile, args)


def edit(request):
    args = {}
    if request.method == 'POST':
        post_email = request.POST['email']
        user_change = Users.objects.get(email=post_email)
        edit_form = EditForm(request.POST, instance=user_change)
        if edit_form.is_valid():
            edit_form.save()
            args['result'] = 'Edit successful!'
            return JsonResponse(args)
        else:
            return JsonResponse(args)
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})
