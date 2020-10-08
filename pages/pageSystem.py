from selenium.webdriver.common.by import By

class Page_system:

    def __init__(self, driver):
        self.driver = driver
        self.item_tab_system = (By.LINK_TEXT, "Calendars")

    def select_item_tab_calendars(self):
        self.driver.find_element(*self.select_item_tab_calendars).click()