from selenium import webdriver
from common.portal_constant import *

class Get():
    driver = webdriver.Firefox()

class LoginPage(Get):
    def __init__(self):
        #self.driver.get("http://portal-uat.tap.finance/merchant/")
        self.driver.get(url1)
        self.driver.implicitly_wait(10)
        self.username = self.driver.find_element_by_xpath(LOGIN_USERNAME_INPUT_XPATH)
        self.password = self.driver.find_element_by_xpath(LOGIN_PASSWORD_INPUT_XPATH)
        self.sign_in = self.driver.find_element_by_xpath(LOGIN_SIGNIN_BUTTON_XPATH)


    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.sign_in.click()
        self.driver.implicitly_wait(10)


class LogoutPage(Get):
    def __init__(self):
        self.driver.implicitly_wait(10)
        self.dropdown = self.driver.find_element_by_xpath(HOME_ACCOUNT_DROPDOWN_XPATH)

    def logout(self):
        self.driver.implicitly_wait(10)
        self.dropdown.click()
        self.logout = self.driver.find_element_by_xpath(HOME_LOGOUT_LINK_XPATH)
        self.logout.click()

class Verify(Get):
    def check_merchant_ui_displays_when_login_with_merchant_account(self):
        assert "home#" in self.driver.current_url
        print("Test Case 001: Login with Merchant Admin account successfully")

    def check_shop_ui_displays_when_login_with_shop_account(self):
        assert "home#" in self.driver.current_url
        try:
            self.orders = self.driver.find_element_by_xpath(HOME_ORDERS_SHOP_ADMIN_TAB_XPATH)
        except IndexError:
            self.orders = None
        print ("\nTest Case 002: Login with Shop Admin account successfully")


    #def verify(self):
     #   assert "home#" in self.driver.current_url

