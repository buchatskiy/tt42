from django.shortcuts import render_to_response
from models import LogRequest


def log_request(request, htmlfile):
    args = {}
    args['entries'] = LogRequest.objects.all().order_by('-date')[:10]
    return render_to_response(htmlfile, args)
