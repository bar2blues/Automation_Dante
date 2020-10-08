from selenium.webdriver.common.by import By

class Page_legal:

    def __init__(self, driver):
        self.driver = driver
        self.item_legal = (By.LINK_TEXT, "Data Processing Agreement Consents")

    def select_item_tab_dpac(self):
        self.driver.find_element(*self.item_legal).click()