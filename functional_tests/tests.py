#!env/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

"""
Functional tests, aka acceptance tests, black-box tests.
User stories as comments
"""

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        User goes to its homepage, notices that the page title and header
        mentions a tod-do list.
        """
        # Check out homepage
        self.browser.get(self.live_server_url)

        # Notice page title and header
        self.assertIn('To-Do', self.browser.title)

        # Invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Types 'buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When hitting enter, the page updates and now
        # the page lists '1: Buy peacock feathers' as an item.
        inputbox.send_keys(Keys.ENTER)
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Look outside to see whether it rains.')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('2: Look outside to see whether it rains.')

        # Now a new user comes along to the site
        self.browser.quit()

        # Start a new session and he doesn't see anything from the previous user.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Look outside to see whether it rains', page_text)

        # New user starts a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        new_user_list_url = self.browser.current_url
        self.assertRegex(new_user_list_url, '/lists/.+')
        self.assertNotEqual(new_user_list_url, user_list_url)

        # And no trace of the first user's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Look outside to see whether it rains', page_text)



        # Test completed
        self.fail('Test completed')
