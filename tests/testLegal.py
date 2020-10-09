from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageLegal import *
from pages.pageDashboard import *
import unittest

class Dante_Legal(unittest.TestCase):
    def setUp(self):
        optionsChrome = Options()
        #optionsChrome.add_argument('headless')
        self.url = 'https://dante.intive.org/Accounts/Authentication/Login'
        self.driver = webdriver.Chrome('chromedriver.exe', options=optionsChrome)
        if self.url == True:
            self.driver.get(
                'https://dante.intive.org/Accounts/Authentication/Login')
        else:
            self.driver.get(
                'https://<user>:<pass>@dante.intive.org')

        self.page_legal = Page_legal(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_legal_dpac(self):
        self.page_dashboard.select_tab('Legal')
        self.page_legal.select_item_tab_dpac()
        self.assertTrue('Data Processing Agreement Consents' in self.driver.find_element_by_id('page-header').text)

    def tearDown(self):
        self.driver.quit()
