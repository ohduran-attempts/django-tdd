"""
This file demonstrates writing tests using the unittest module.
They will pass when you run 'manage.py test'
"""
from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string

from lists.views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertTrue(response.content.strip().startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

        # expected_html = render_to_string('home.html')
        # self.assertEqual(response.content, expected_html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
