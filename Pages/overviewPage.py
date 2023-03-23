from selenium.webdriver.common.by import By

from Locators.locators import OverviewPageLocators


class overviewPage:
    def __init__(self, driver):
        self.driver = driver


    def finish_button(self):
        self.driver.find_element(By.ID, OverviewPageLocators.finishButton_Id).click()
