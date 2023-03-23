from selenium.webdriver.common.by import By

from Locators.locators import LoginPageLocators


class Loginpage:

    def __init__(self, driver):
        self.driver = driver
        # self.username_field_id = "user-name"
        # self.password_field_id = "password"
        # self.login_button_id = "Login-button"


    def enter_username(self, username):
        self.driver.find_element(By.ID, LoginPageLocators.username_field_id).clear()
        self.driver.find_element(By.ID, LoginPageLocators.username_field_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, LoginPageLocators.password_field_id).clear()
        self.driver.find_element(By.ID, LoginPageLocators.password_field_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, LoginPageLocators.login_button_id).click()