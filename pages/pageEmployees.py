from selenium.webdriver.common.by import By


class Page_employees:

    def __init__(self, driver):
        self.driver = driver
        self.item_employees = (
            By.XPATH, '//*[@id="main-menu"]/ul[1]/li[3]/ul/li[8]/a')
        self.search_box = (By.NAME, 'search')
        self.search_icon_button = (By.XPATH,
                                   '/html/body/div/div[1]/div[2]/div/nav/div/div[1]/div/div/span')

    def select_item_tab_employees(self):
        select_item = self.driver.find_element(*self.item_employees)
        select_item.click()

    def search_by_box(self, name):
        box_employees = self.driver.find_element(*self.search_box)
        box_employees.send_keys(name)
        search_employees_icon_button = self.driver.find_element(
            *self.search_icon_button)
        search_employees_icon_button.click()
