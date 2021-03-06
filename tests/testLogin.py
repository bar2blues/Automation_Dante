from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageLogin import *
import unittest
import time


class Dante_Login(unittest.TestCase):

    def setUp(self):
        optionsChrome = Options()
        optionsChrome.add_argument('headless')
        self.url = 'https://dante.intive.org/Accounts/Authentication/Login'
        self.driver = webdriver.Chrome('chromedriver.exe', options=optionsChrome)
        if self.url == True:
            self.driver.get(
                'https://dante.intive.org/Accounts/Authentication/Login')
        else:
            self.driver.get(
                'https://<user>:<pass>@dante.intive.org')

        self.page_login = Page_login(self.driver)
        self.driver.implicitly_wait(5)

    @unittest.skipIf('https://<user>:<pass>@dante.intive.org' == True, 'Se saltea el test por NO estar conectado a la VPN de  Intive')
    def test_login(self):
        self.page_login.login('<user>', '<pass>')

    def tearDown(self):
        self.driver.quit()
