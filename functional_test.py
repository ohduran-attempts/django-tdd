#!env/bin/python
import unittest
from selenium import webdriver

"""
Functional tests, aka acceptance tests, black-box tests.
User stories as comments
"""

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        User goes to its homepage, notices that the page title and header
        mentions a tod-do list.
        """
        # Check out homepage
        self.browser.get('http://localhost:8000')

        # Notice page title and header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Test completed')

        # Invited to enter a to-do item straight away

        # Types 'buy peacock feathers' into a text box

        # When hitting enter, the page updates and now
        # the page lists '1: Buy peacock feathers' as an item.

if __name__ == '__main__':
    unittest.main()
