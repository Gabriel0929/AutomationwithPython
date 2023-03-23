from selenium.webdriver.common.by import By

from Locators.locators import completePageLocators


class completePage:
    def __init__(self, driver):
        self.driver = driver


    def complete_text(self):
        self.driver.find_element(By.XPATH, completePageLocators.CompleteTextPath).text


