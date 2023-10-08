import unittest
from flask_cl import *

class TestFlask(unittest.TestCase):
    def test_route_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Welcome", response.data)

    def test_route_help(self):
        self.app = app.test_client()
        response = self.app.get('/get_help', follow_redirects=True)
        self.assertIn(b"Welcome", response.data)

    def test_route_company(self):
        self.app = app.test_client()
        response = self.app.get('/get_company/NFLX', follow_redirects=True)
        self.assertIn(b"Welcome", response.data)

    def test_route_date(self):
        self.app = app.test_client()
        response = self.app.get('/get_date/2020-04-01', follow_redirects=True)
        self.assertIn(b"Welcome", response.data)
    
    def test_route_404(self):
        self.app = app.test_client()
        response = self.app.get('/peepee', follow_redirects=True)
        self.assertIn(b"ERROR", response.data)

    def test_route_500(self):
        self.app = app.test_client()
        response = self.app.delete('/', follow_redirects=True)
        self.assertIn(b"405 Method Not Allowed", response.data)
