from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import unittest

PAGE_ADDRESS = 'http://127.0.0.1:8000'


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    """
    def test_login_menu_presence(self):
        self.browser.get( PAGE_ADDRESS )
        self.assertIn('Log In', self.browser.page_source)
    """

    """
    def test_click_login_in_menu(self):
        self.browser.get( PAGE_ADDRESS )
        menu_item = self.browser.find_element_by_css_selector( '[href$="login/"]' )
        menu_item.click()
        self.browser.implicitly_wait(5)
        self.assertIn('Log In Form', self.browser.title)
    """

    def test_redirect_after_logging(self):
        self.browser.get( PAGE_ADDRESS )
        login_menu_item = self.browser.find_element_by_css_selector( '[href*="login/"]' )
        login_menu_item.click()
        self.browser.implicitly_wait(5)

        inputbox_username = self.browser.find_element_by_css_selector( '[name="username"]' )
        inputbox_password = self.browser.find_element_by_css_selector( '[name="password"]' )

        inputbox_username.send_keys('sean')
        inputbox_password.send_keys('sean')
        inputbox_password.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        self.assertIn('Django test', self.browser.title)
        logout_menu_item = self.browser.find_element_by_css_selector( '[href*="logout"]' )


        self.fail('111: Finish the test successfully')


if __name__ == '__main__':
    unittest.main()



"""    >>>   CSS and design   test examples

class NewVisitorTest(LiveServerTestCase):
    [...]
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


"""    >>>   Deployment   test examples

import sys
[...]
class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        [...]


"""


"""     >>>   My Tests
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
self.browser.current_url

from django.test import LiveServerTestCase
      self.browser.get( self.live_server_url )     # live_server_url 

class NewVisitorTest(StaticLiveServerTestCase):   cls.server_url

self.assertContains(response, 'itemey 1')
   вместо
assertIn/response.content.decode()   dance

self.assertTemplateUsed(response, 'list.html')
self.assertRegex(francis_list_url, '/lists/.+')


from django.test import TestCase
class SimpleTest(TestCase):
    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)

"""
