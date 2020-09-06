from selenium.webdriver.common.by import By


class Page_dashboard:

    def __init__(self, driver):
        self.driver = driver

    def select_tab(self, nameTab):
        nav_tab = self.driver.find_element(By.LINK_TEXT, nameTab)
        nav_tab.click()
