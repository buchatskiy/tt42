from django.shortcuts import render_to_response
from models import LogRequest
from django.contrib import auth


def log_request(request, htmlfile):
    args = {}
    args['username'] = auth.get_user(request).username
    args['entries'] = LogRequest.objects.all().order_by('-date')[:10]
    return render_to_response(htmlfile, args)
