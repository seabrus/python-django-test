import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import unittest
from unittest import skip

PAGE_ADDRESS = 'http://127.0.0.1:8000'


class LoginTest(unittest.TestCase):
    __name__ = 'foo'     # for the "skip" decorator: http://stackoverflow.com/questions/22204660/python-mock-wrapsf-problems
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    @skip
    def test_login_menu_presence(self):
        self.browser.get( PAGE_ADDRESS )
        self.assertIn('Log In', self.browser.page_source)
        self.fail('Success:  test_login_menu_presence  is passed')

    @skip
    def test_click_login_in_menu(self):
        self.browser.get( PAGE_ADDRESS )
        login_menu_item = self.browser.find_element_by_css_selector( '[href*="login/"]' )
        login_menu_item.click()
        time.sleep(15)
        self.assertIn('Log In Form', self.browser.title)
        self.fail('Success:  test_click_login_in_menu  is passed')


    def test_redirect_after_logging(self):
        self.browser.get( PAGE_ADDRESS )
        login_menu_item = self.browser.find_element_by_css_selector( '[href*="login/"]' )
        login_menu_item.click()

        inputbox_username = self.browser.find_element_by_css_selector( '[name="username"]' )
        inputbox_password = self.browser.find_element_by_css_selector( '[name="password"]' )

        inputbox_username.send_keys('sean')
        inputbox_password.send_keys('sean')
        inputbox_password.send_keys(Keys.ENTER)

        self.assertIn('Django test', self.browser.title)
        logout_menu_item = self.browser.find_element_by_css_selector( '[href*="logout"]' )

        self.fail('Success:  test_redirect_after_logging  is passed')


if __name__ == '__main__':
    unittest.main()



"""   >>>   ESCAPE FUNCTION
from django.utils.html import escape
[...]
        expected_error = escape("You can't have an empty list item")   # => escapes the apostrophe
        self.assertContains(response, expected_error)
"""



"""   >>>   @SKIP
http://chimera.labs.oreilly.com/books/1234000000754/ch10.html#_skipping_a_test
from unittest import skip       # skip the test
[...]
    __name__ = 'foo'     # for the "skip" decorator: http://stackoverflow.com/questions/22204660/python-mock-wrapsf-problems
    @skip
    def test_cannot_add_empty_list_items(self):

"""
"""   KEYS
    She hits Enter
    self.browser.find_element_by_id('id_new_item').send_keys('\n')   # <<< ENTER

"""


"""    >>>   CSS and DESIGN   test examples
http://chimera.labs.oreilly.com/books/1234000000754/ch07.html#_what_to_functionally_test_about_layout_and_style

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        [...]

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to check out its homepage
        self.browser.get(self.live_server_url)     #       <<< self.live_server_url

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
"""


"""    >>>   DEPLOYMENT   test examples
http://chimera.labs.oreilly.com/books/1234000000754/ch08.html#_as_always_start_with_a_test

import sys
[...]
class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod                        # setUpClass is a similar method to setUp, it's provided by unittest
    def setUpClass(cls):                #    -- vs. setUpTestData(cls) (it's new as of v. 1.8): 
        for arg in sys.argv:             # https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase.setUpTestData
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url                  # and then substitute "server_url" for "live_server_url" in the code

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        [...]


"""


"""     >>>   MY TESTS
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Forms, Messages, and AJAX', header_text)

class NamePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_your_name_form(self):
        # Checking name field initials
        inputbox_name = self.browser.find_element_by_id('id_your_name')
        self.assertEqual(
                inputbox_name.get_attribute('placeholder'),
                'e.g., Ann Smith'
        )
        # Checking  date field initials
        inputbox_date = self.browser.find_element_by_id('id_date_field')
        self.assertEqual(
                inputbox_date.get_attribute('value'),
                '2015-11-20'
        )

        # Submitting the form with default values - should raise error, and display its message in red on the page 
        inputbox_name.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        error_div = self.browser.find_element_by_class_name('form-field-error')
        self.assertIn(
                'Please enter your name',
                error_div.text
        )
        self.assertEqual(
                'rgb(255, 0, 0)',   # red
                self.browser.execute_script('var cs = window.getComputedStyle(arguments[0], null); return cs.color;', error_div)
        )


        # Submitting the form with a wrong name (1 letter) - should raise error, and display its message in red on the page 
        inputbox_name = self.browser.find_element_by_id('id_your_name')
        inputbox_name.send_keys('A')
        inputbox_name.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        error_div = self.browser.find_element_by_class_name('form-field-error')
        self.assertIn(
                'Ensure this value has at least 2 characters (it has 1).',
                error_div.text
        )
        self.assertEqual(
                'rgb(255, 0, 0)',   # red
                self.browser.execute_script('var cs = window.getComputedStyle(arguments[0], null); return cs.color;', error_div)
        )

        # Submitting the form with a correct name
        inputbox_name = self.browser.find_element_by_id('id_your_name')
        inputbox_name.send_keys('Boris')
        inputbox_name.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        with self.assertRaises( NoSuchElementException ):
            error_div = self.browser.find_element_by_class_name('form-field-error')
"""


"""   >>>   E X A M P L E S
self.browser.page_source
page_text = self.browser.find_element_by_tag_name('body').text

francis_list_url = self.browser.current_url
self.assertRegex(francis_list_url, '/lists/.+')

from django.test import LiveServerTestCase
      self.browser.get( self.live_server_url )     # live_server_url 

class NewVisitorTest(StaticLiveServerTestCase):   cls.server_url

self.assertContains(response, 'itemey 1')
   instead of
assertIn/response.content.decode(), ...   dance

self.assertTemplateUsed(response, 'list.html')

self.assertNotEqual(francis_list_url, edith_list_url)
self.assertNotIn('Buy peacock feathers', page_text)

from django.test import TestCase
class SimpleTest(TestCase):
    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)

"""
