import unittest
from app import *

class TestFlask(unittest.TestCase):
    def test_route_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Home Page", response.data)

    def test_research(self):
        self.app = app.test_client()
        response = self.app.get('/research', follow_redirects=True)
        self.assertIn(b"Select company to display table", response.data)

    def test_play(self):
        self.app = app.test_client()
        response = self.app.get('/play', follow_redirects=True)
        self.assertIn(b"Total Money Invested: $", response.data)

    def test_route_help(self):
        self.app = app.test_client()
        response = self.app.get('/help', follow_redirects=True)
        self.assertIn(b"How to use our site:", response.data)
    
    def test_route_404(self):
        self.app = app.test_client()
        response = self.app.get('/goodmorning', follow_redirects=True)
        self.assertIn(b"404 PAGE NOT FOUND", response.data)

    def test_route_500(self):
        self.app = app.test_client()
        response = self.app.delete('/', follow_redirects=True)
        self.assertIn(b"500 BACKEND ERROR", response.data)

if __name__ == "__main__":
    unittest.main()