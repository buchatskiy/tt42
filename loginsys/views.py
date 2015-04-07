from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from loginsys.form import MyRegistrationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from users.models import Users


def login(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            try:
                User.objects.get(username=username)
                args['login_error'] = 'Invalid Password'
                args['username_old'] = username
                return render_to_response('login.html', args)
            except:
                args['login_error'] = 'User not found'
                return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['username'] = auth.get_user(request).username
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            user = Users(email=auth.get_user(request).email,
                         first_name=auth.get_user(request).first_name or "-",
                         last_name=auth.get_user(request).last_name or "-",
                         date_birth="1990-01-01"
                         )
            user.save()
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
