from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from Locators.locators import completePageLocators


class completePage:
    def __init__(self, driver):
        self.driver = driver


    # def complete_text(self):
    #     self.driver.find_element(By.XPATH, completePageLocators.CompleteTextPath).text


    def complete_text(self) -> WebElement:
        return self.driver.find_element(By.ID, completePageLocators.Complete_textID).find_element(By.CLASS_NAME,completePageLocators.Complete_textClassId)





