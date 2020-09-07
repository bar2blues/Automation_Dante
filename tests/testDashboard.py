from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageDashboard import *
import unittest


class Dante_Dashboard(unittest.TestCase):

    def setUp(self):
        optionsChrome = Options()
        self.url = 'https://dante.intive.org/Accounts/Authentication/Login'
        self.driver = webdriver.Chrome('chromedriver.exe', options=optionsChrome)
        if self.url == True:
            self.driver.get(
                'https://dante.intive.org/Accounts/Authentication/Login')
        else:
            self.driver.get(
                'https://federico.barderi:Clave-19@dante.intive.org')

        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)


    def test_vacation_remain(self):
        self.page_dashboard.select_my_vacation_balance()
        self.assertTrue('My Vacation Balance' in self.page_dashboard.return_my_vacation_balance())

    def test_overtime_bank(self):
        self.page_dashboard.select_overtime_bank()
        self.assertTrue('Overtime Bank' in self.page_dashboard.return_overtime_bank())

    def tearDown(self):
        self.driver.quit()
