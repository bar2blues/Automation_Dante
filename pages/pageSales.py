from selenium.webdriver.common.by import By

class Page_sales:

    def __init__(self, driver):
        self.driver = driver
        self.item_customer = (By.LINK_TEXT, "Customers")

    def select_item_tab_customers(self):
        self.driver.find_element(*self.item_customer).click()

