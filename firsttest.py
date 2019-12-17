import time
from selenium import webdriver
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Fiza.Bajwa\\Desktop\\chromedriver_win32\\geckodriver.exe")
        self.driver.get('https://kayak.qtestnet.com')

    def test_Login(self):
                # Find and fill the email field
         email_elem = self.driver.find_element_by_css_selector("[name='j_username'][type='text']")

         email_elem.send_keys('fiza.bajwa@arbisoft.com')
                #Find and fill the password field
         pwd_elem = self.driver.find_element_by_css_selector("[name='j_password'][type='password']")
         pwd_elem.send_keys('')
                # Find and click the submit button

         subnit_elem = self.driver.find_element_by_css_selector('#loginButton')
         subnit_elem.click()
         time.sleep(10)
         self.assertIn('Test Execution',self.driver.title )

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
