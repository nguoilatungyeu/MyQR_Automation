import unittest
from actions.action_login_page import *

class MyQRLoginTestcase(unittest.TestCase):
    def setUp(self):
        self.login_page = LoginPage()

    def test_tc001_login_with_valid_merchat_account(self):
        """
        @author: tu.le                         date: 29-Dec-2017
        @updated:                              date:
        @summary: Verify that user can login successfully with valid Merchant Admin account
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Enter valid username
            3. Enter valid password
            4. Click on "Login" button
        @expected:
            Merchant Home page displays
        """

        self.login_page.login(CoreMerchantUserName,CoreMerchantPassword)
        self.check = Verify()
        self.check.check_merchant_ui_displays_when_login_with_merchant_account()
        self.logout_page = LogoutPage()
        self.logout_page.logout()

    def test_tc002_login_with_valid_shop_account(self):
        """
        @author: tu.le                         date: 29-Dec-2017
        @updated:                         date:
        @summary: Verify that user can login successfully with valid Shop Admin account
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Enter valid username
            3. Enter valid password
            4. Click on "Login" button
        @expected:
            Shop Home page displays (check that Orders tab display)
        """

        self.login_page.login(CoreShopUserName,CoreShopPassword)
        self.check = Verify()
        self.check.check_shop_ui_displays_when_login_with_shop_account()
        self.logout_page = LogoutPage()
        self.logout_page.logout()



    #def tearDown(self):
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()



