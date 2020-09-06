from selenium.webdriver.common.by import By


class Page_login:
    def __init__(self, driver):
        self.driver = driver
        self.user_box = (By.ID, 'login')
        self.pass_box = (By.ID, 'password')
        self.submit_button = (By.ID, 'submit-button')

    def login(self, user_name, password):
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)
