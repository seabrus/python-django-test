from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_page_title(self):
        self.browser.get('http://127.0.0.1:8000/dj/your-name/')

        self.assertIn('Learning Forms', self.browser.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()

