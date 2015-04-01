from django.test import TestCase

from django.test import TestCase
from models import LogRequest
from django.test.client import Client


class MiddlewareTest(TestCase):
    def test_httprequest(self):
        client = Client()
        response = client.get('/')

        log_entry = LogRequest.objects.get(path='/')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.request_method, 'GET')
