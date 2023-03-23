from selenium.webdriver.common.by import By

from Locators.locators import checkoutPageLocators


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self, name):
        self.driver.find_element(By.ID, checkoutPageLocators.firstName_Id).clear()
        self.driver.find_element(By.ID, checkoutPageLocators.firstName_Id).send_keys(name)

    def last_name(self, lastname):
        self.driver.find_element(By.ID, checkoutPageLocators.lastName_Id).clear()
        self.driver.find_element(By.ID, checkoutPageLocators.lastName_Id).send_keys(lastname)

    def zip_code(self, zip):
        self.driver.find_element(By.ID, checkoutPageLocators.zip_Id).clear()
        self.driver.find_element(By.ID, checkoutPageLocators.zip_Id).send_keys(zip)

    def continue_button(self):
        self.driver.find_element(By.ID, checkoutPageLocators.continueButton_Id).click()
