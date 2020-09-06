from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageEmployees import *
from pages.pageDashboard import *
from pages.pageTimeTracking import *
from pages.pageLogin import *
import unittest


class Dante(unittest.TestCase):

    def setUp(self):
        optionsChrome = Options()
        optionsChrome.add_argument('headless')
        self.url = 'https://dante.intive.org/Accounts/Authentication/Login'
        self.driver = webdriver.Chrome('Tests/drivers/chromedriver.exe', options=optionsChrome)
        if self.url == True:
            self.driver.get(
                'https://dante.intive.org/Accounts/Authentication/Login')
        else:
            self.driver.get('https://<user>:<pass>@dante.intive.org')

        self.page_login = Page_login(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.page_employees = Page_employees(self.driver)
        self.page_timetracking = Page_timeTracking(self.driver)
        self.driver.implicitly_wait(5)

    @unittest.skipIf('https://<user>:<pass>@dante.intive.org',
                     'Se saltea el test por NO estar conectado a la VPN de  Intive')
    def test_login(self):
        self.page_login.login('<user>', '<pass>')

    def test_tab_employees(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_employees()
        self.page_employees.search_by_box('federico')
        self.assertTrue('Employees' in self.driver.find_element_by_xpath(
            '//*[@id="page-header"]/a').text)

    def test_tab_timeTracking(self):
        self.page_dashboard.select_tab('Time Tracking')
        self.page_timetracking.select_item_tab_timeTracking('Absence Type')
        self.assertTrue('Absence Type' in self.driver.find_element(By.ID,
                                                                   'page-header').text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
