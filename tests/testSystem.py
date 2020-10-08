from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageSystem import *
from pages.pageDashboard import *
import unittest

class Dante_System(unittest.TestCase):
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
                'https://federico.barderi:Clave-20@dante.intive.org')

        self.page_system = Page_system(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_system_calendar(self):
        self.page_dashboard.select_tab('System')
        self.page_system.select_item_tab_calendars()
        self.assertTrue('Calendars' in self.driver.find_element_by_id('page-header').text)

    def tearDown(self):
        self.driver.quit()