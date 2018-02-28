import unittest
from actions.action_merchant_main_page import *

class MyQRMerchantMainPageTestcase(unittest.TestCase):
    def setUp(self):
        self.login_page = LoginPage()
        self.login_page.login(CoreMerchantUserName, CoreMerchantPassword)

    def test_tc007_verify_add_product_function(self):
        """
        @author: tu.le                         date: Feb-16-2018
        @updated:                         date:
        @summary: Verify that user can add valid product successful
        @precondition: Delete product with ID = testID2 if this product is already existed
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Login with valid username/password of Merchant
            3. Click on Product tab
            4. Click on 'Create new product' button
            5. Add product with ID = testID2

        @expected:
            Product with ID = testID2 show on table
        """
        self.add_product = AddProduct()
        self.add_product.add_new_valid_product()
        self.add_product.verify_product_show_on_table_when_user_adds_valid_product()
        self.logout_page = LogoutPage()
        self.logout_page.logout()

if __name__ == "__main__":
    unittest.main()