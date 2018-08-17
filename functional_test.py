#!env/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        print(rows.text)
        self.assertIn(
            '1: Buy peacock feathers',
            [row.text for row in rows],
            "new to-do item did not show")

        # Test completed
        self.fail('Test completed')



if __name__ == '__main__':
    unittest.main()
