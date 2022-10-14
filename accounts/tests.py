from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.models import User

class AccountTestCase(TestCase):
    testing_url = 'http://localhost:8000/'

    def setUp(self):
        """
        Sets up the webpage - be sure to have server running
        """
        self.browser = webdriver.Firefox()
        self.browser.get(self.testing_url)
        
    def login(self):
        """
        Logs in with a pre made account
        """
        user = self.browser.find_element('id','id_username')
        user.send_keys('test')
        passw = self.browser.find_element('id','id_password')
        passw.send_keys('peanut')
        self.browser.find_element('xpath', "//button[contains(., 'Login')]").click()

    def test_there_is_homepage(self):
        """
        Checks to see if the homepage comes up after logging in

        - might be an error (cannnot iterate...too fast to see actual error... time.sleep?)
        """
        self.login()
        self.assertIn ('Add a new note: ',self.browser.page_source)

    def test_create_new_user(self):
        """
        Creates a new users then logs out

        - Need to create a delete account button
        """
        if self.check_exists_by_xpath("//a[contains(., 'Sign Up')]"):
            self.browser.find_element('xpath', "//a[contains(., 'Sign Up')]").click()
        username = self.browser.find_element('id','id_username')
        username.send_keys('newuser')
        password = self.browser.find_element('id','id_password1')
        password.send_keys('testing')
        password_confirmation = self.browser.find_element('id','id_password2')
        password_confirmation.send_keys('testing')
        self.browser.find_element('xpath', "//button[contains(., 'Create account')]").click()
        self.logout()


    def check_exists_by_xpath(self, xpath):
        """
        Checking to see if an element is there by xpath
        """
        try:
            self.browser.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def logout(self):
        """
        Logs current user out from site
        """
        self.browser.get(self.testing_url + 'home')
        if self.check_exists_by_xpath("//a[contains(., 'Logout')]"):
            self.browser.find_element('xpath', "//a[contains(., 'Logout')]").click()

    def tearDown(self):
        """
        Logs user out then shuts down the browser
        """
        self.logout()
        self.browser.quit()