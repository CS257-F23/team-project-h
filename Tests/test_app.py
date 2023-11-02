import unittest
from app import *

class TestFlask(unittest.TestCase):
    def test_route_homepage(self):
        '''Test for the homepage.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"Home Page", response.data)

    def test_research(self):
        '''Test for the research page. 
           It should display the given message when a user enters the page.'''
        self.app = app.test_client()
        response = self.app.get('/research', follow_redirects=True)
        self.assertIn(b"Select company to display table", response.data)

    def test_play(self):
        '''Test for the play investment page.'''
        self.app = app.test_client()
        response = self.app.get('/play', follow_redirects=True)
        self.assertIn(b"Total Money Invested: $", response.data)

    def test_route_help(self):
        '''Test for the help page. '''
        self.app = app.test_client()
        response = self.app.get('/help', follow_redirects=True)
        self.assertIn(b"How to use our site:", response.data)
    
    def test_route_404(self):
        '''Test for the 404 page, given a user enters an invalid url. '''
        self.app = app.test_client()
        response = self.app.get('/goodmorning', follow_redirects=True)
        self.assertIn(b"404 PAGE NOT FOUND", response.data)

    def test_route_500(self):
        '''Test for the 500 page, given a backend error. '''
        self.app = app.test_client()
        response = self.app.delete('/', follow_redirects=True)
        self.assertIn(b"405 Method Not Allowed", response.data)

    def test_route_research_post(self):
        pass

    def test_route_play_post(self):
        pass





if __name__ == "__main__":
    unittest.main()