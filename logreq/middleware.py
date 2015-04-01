from models import LogRequest


class SaveRequests(object):
    def process_request(self, request):
        log_entry = LogRequest(
            request_method=request.META.get('REQUEST_METHOD', '?')[:20],
            path=request.path[:256]
        )
        log_entry.save()
