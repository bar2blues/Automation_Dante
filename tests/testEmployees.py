from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.pageEmployees import *
from pages.pageDashboard import *
import unittest

class Dante_Employees(unittest.TestCase):

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

        self.page_employees = Page_employees(self.driver)
        self.page_dashboard = Page_dashboard(self.driver)
        self.driver.implicitly_wait(5)

    def test_tab_employees_my_resume(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_my_resume()
        self.assertTrue('My Resume' in self.driver.find_element_by_xpath('//*[@id="resume-header"]/div[1]/h3').text)

    def test_tab_employees_my_surveys(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_my_surveys()
        self.assertTrue('My Surveys' in self.driver.find_element_by_xpath('//*[@id="page-header"]').text)

    def test_tab_employees_employees(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_employees()
        self.page_employees.search_by_box('federico')
        self.assertTrue('Employees' in self.driver.find_element_by_xpath(
            '//*[@id="page-header"]/a').text)

    def test_tab_employees_org_units(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_org_units()
        self.assertTrue('Org Units' in self.driver.find_element_by_xpath('//*[@id="page-header"]').text)

    def test_tab_employees_org_chart(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_org_chart()
        self.assertTrue('Org Chart' in self.driver.find_element_by_xpath('//*[@id="page-header"]').text)

    def test_tab_employees_org_chart_director(self):
        self.page_dashboard.select_tab('Employees')
        self.page_employees.select_item_tab_org_chart()
        self.page_employees.select_item_tab_org_chart_director()
        self.assertTrue('Francisco Martín Ronconi' in
                        self.driver.find_element_by_xpath(
                            '//*[@id="common-dialog-show-model-useremployeehubviewmodel"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]').text)

    # CLOSE

    def tearDown(self):
        self.driver.quit()
