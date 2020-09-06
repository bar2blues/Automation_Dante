from selenium.webdriver.common.by import By


class Page_timeTracking:

    def __init__(self, driver):
        self.driver = driver

    def select_item_tab_timeTracking(self, itemLinkName):
        item_timetracking = self.driver.find_element(By.LINK_TEXT, itemLinkName)
        item_timetracking.click()
