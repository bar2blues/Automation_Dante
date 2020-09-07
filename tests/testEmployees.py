from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageEmployees import *
from pages.pageDashboard import *
import unittest

class Dante_Employees(unittest.TestCase):

    def setUp(self):
        optionsChrome = Options()
        self.url = 'https://dante.intive.org/Accounts/Authentication/Login'
        self.driver = webdriver.Chrome('chromedriver.exe', options=optionsChrome)
        if self.url == True:
            self.driver.get(
                'https://dante.intive.org/Accounts/Authentication/Login')
        else:
            self.driver.get(
                'https://<user>:<pass>@dante.intive.org')

        self.page_employees = Page_employees(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_employees(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_employees()
        self.page_employees.search_by_box('federico')
        self.assertTrue('Employees' in self.driver.find_element_by_xpath(
            '//*[@id="page-header"]/a').text)

    def tearDown(self):
        self.driver.quit()
