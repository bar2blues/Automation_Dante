from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageSales import *
from pages.pageDashboard import *
import unittest

class Dante_Sales(unittest.TestCase):
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

        self.page_sales = Page_sales(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_sales_customers(self):
        self.page_dashboard.select_tab('Sales')
        self.page_sales.select_item_tab_customers()
        self.assertTrue('Customers' in self.driver.find_element_by_xpath(
            '//*[@id="page-header"]').text)

    def tearDown(self):
        self.driver.quit()