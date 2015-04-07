from django.shortcuts import render_to_response, redirect
from users.models import Users
from forms import EditForm
from django.core.context_processors import csrf
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def main(request, htmlfile):
    username = auth.get_user(request).username
    if username:
        first_user = Users.objects.get(email=auth.get_user(request).email)
    else:
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
    args['username'] = username
    return render_to_response(htmlfile, args)

@login_required
def edit_page(request, htmlfile):
    args = {}
    args.update(csrf(request))
    username = auth.get_user(request).username
    if username:
        first_user = Users.objects.get(email=auth.get_user(request).email)
    else:
        first_user = Users.objects.all()[0]
    args['form'] = EditForm(instance=first_user)
    args['username'] = username
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
