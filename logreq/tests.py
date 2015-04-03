import unittest
from models import LogRequest
from django.test.client import Client

"""
class MiddlewareTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        self.client.get('/')
        log_entry = LogRequest.objects.get(path='/')
        self.assertNotEquals(log_entry, None)
        self.assertEquals(log_entry.request_method, 'GET')"""
