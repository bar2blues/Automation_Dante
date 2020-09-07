from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageTimeTracking import *
from pages.pageDashboard import *
import unittest


class Dante_TimeTracking(unittest.TestCase):

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

        self.page_timetracking = Page_timeTracking(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_timeTracking(self):
        self.page_dashboard.select_tab('Time Tracking')
        self.page_timetracking.select_item_tab_timeTracking('Absence Type')
        self.assertTrue('Absence Type' in self.driver.find_element(By.ID,
                                                                   'page-header').text)

    def tearDown(self):
        self.driver.quit()
