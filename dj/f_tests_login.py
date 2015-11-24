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
    def test_login_click_in_menu(self):
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



        self.fail('GOOD news: Finish the test successfully')




    """
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Forms, Messages, and AJAX', header_text)

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




if __name__ == '__main__':
    unittest.main()


"""
driver.page_source
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
"""
