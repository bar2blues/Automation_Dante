from selenium.webdriver.common.by import By


class Page_employees:

    def __init__(self, driver):
        self.driver = driver
        self.item_employees = (
            By.XPATH, '//*[@id="main-menu"]/ul[1]/li[3]/ul/li[8]/a')
        self.search_box = (By.NAME, 'search')
        self.search_icon_button = (By.XPATH,
                                   '/html/body/div/div[1]/div[2]/div/nav/div/div[1]/div/div/span')
        self.item_my_resume = (By.XPATH, '//*[@id="main-menu"]/ul[1]/li[3]/ul/li[3]/a')
        self.close_popup_resume = (By.XPATH, '//*[@id="suggestedSkillsModal"]/div/div/div/div[1]/button')


    def select_item_tab_employees(self):
        self.driver.find_element(*self.item_employees).click()

    def search_by_box(self, name):
        box_employees = self.driver.find_element(*self.search_box)
        box_employees.send_keys(name)
        search_employees_icon_button = self.driver.find_element(
            *self.search_icon_button)
        search_employees_icon_button.click()

    def select_item_tab_my_resume(self):
        self.driver.find_element(*self.item_my_resume).click()
        self.driver.find_element(*self.close_popup_resume).click()



