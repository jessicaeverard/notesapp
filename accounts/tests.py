from django.test import TestCase
from selenium import webdriver


class AccountTestCase(TestCase):
    testing_url = 'http://localhost:8000/'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.testing_url)
        username = self.browser.find_element('id','id_username')
        username.send_keys('test')
        password = self.browser.find_element('id','id_password')
        password.send_keys('peanut')
        self.browser.find_element('xpath', "//button[contains(., 'Login')]").click()

    def test_there_is_homepage(self):
        self.assertIn ('Add a new note: ',self.browser.page_source)

    def tearDown(self):
        self.browser.quit()