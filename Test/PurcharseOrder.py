import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Pages.ProductPage import ProductPage
from Pages.ShoppingcartPage import ShoppingcartPage
from Pages.checkoutPage import CheckoutPage
from Pages.completePage import completePage
from Pages.loginpage import Loginpage
from Pages.overviewPage import overviewPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=cls.options)

    def test_valid_login(self):
        expectedCompleteTest = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = Loginpage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        time.sleep(2)
        products = ProductPage(driver)
        products.select_product1()
        products.select_cart()
        shoppingcart = ShoppingcartPage(driver)
        shoppingcart.shopping_cart()
        time.sleep(2)
        checkout = CheckoutPage(driver)
        checkout.first_name("Gabriel")
        checkout.last_name("Gonzales")
        checkout.zip_code("1234")
        checkout.continue_button()
        overview = overviewPage(driver)
        overview.finish_button()
        complete = completePage(driver)
        print(complete.complete_text())
        self.assertEqual(complete.complete_text(), expectedCompleteTest, "First value and second value are not equal !")
        time.sleep(2)





        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()