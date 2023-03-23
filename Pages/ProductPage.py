from selenium.webdriver.common.by import By

from Locators.locators import ProductPageLocators


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product1(self):
        self.driver.find_element(By.ID, ProductPageLocators.backpack_Id).click()

    def select_cart(self):
        self.driver.find_element(By.ID, ProductPageLocators.shoppingCart_Id).click()


