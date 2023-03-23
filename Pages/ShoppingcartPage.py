from selenium.webdriver.common.by import By

from Locators.locators import ShoppingcartPageLocators


class ShoppingcartPage:
    def __init__(self, driver):
        self.driver = driver

    def shopping_cart(self):
        self.driver.find_element(By.ID, ShoppingcartPageLocators.checkoutButton_Id).click()



