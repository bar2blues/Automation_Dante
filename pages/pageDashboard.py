from selenium.webdriver.common.by import By


class Page_dashboard:

    def __init__(self, driver):
        self.driver = driver

    def select_tab(self, nameTab):
        nav_tab = self.driver.find_element(By.LINK_TEXT, nameTab)
        nav_tab.click()

    def select_my_vacation_balance(self):
        self.driver.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div/div[1]/div/div/div[2]/div[2]/div/a/h2').click()

    def return_my_vacation_balance(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-header"]/a').text


