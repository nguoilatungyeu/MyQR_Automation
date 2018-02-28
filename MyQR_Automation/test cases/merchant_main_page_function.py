import unittest
from actions.action_merchant_main_page import *

class MyQRMerchantMainPageTestcase(unittest.TestCase):
    def setUp(self):
        self.login_page = LoginPage()
        self.login_page.login(CoreMerchantUserName, CoreMerchantPassword)

    def test_tc003_verify_search_function(self):
        """
        @author: tu.le                         date: Jan-5-2018
        @updated:                         date:
        @summary: Verify that search function work correctly
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Login with valid username/password of Merchant
            3. Click on Product tab
            4. Enter text in search textbox
            5. Press Enter key
        @expected:
            Result table only show correct records
        """

        self.search_product = SearchProduct()
        self.search_product.search_product(search_id)
        self.search_product.verify_search_result_table_show_only_correct_records(search_id)

        self.logout_page = LogoutPage()
        self.logout_page.logout()

    def test_tc004_verify_delete_first_product_function(self):
        """
        @author: tu.le                         date: Feb-16-2018
        @updated:                         date:
        @summary: Verify that delete first product function work correctly
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Login with valid username/password of Merchant
            3. Click on Product tab
            4. Check on first checkbox
            5. Expand Action dropdown and select Delete
            6. Click on Delete on Confirm popup
        @expected:
            First product is removed from table
        """
        self.delete_one_product = DeleteProduct()
        deleted_id = self.delete_one_product.delete_first_product()
        self.delete_one_product.verify_deleted_product_not_show_on_table(deleted_id)

        self.logout_page = LogoutPage()
        self.logout_page.logout()

    def test_tc005_verify_delete_multi_product_function(self):
        """
        @author: tu.le                         date: Feb-21-2018
        @updated:                         date:
        @summary: Verify that delete multi products function work correctly
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Login with valid username/password of Merchant
            3. Click on Product tab
            4. Enter search key into Search textbox
            5. Check on check all checkbox
            6. Expand Action dropdown and select Delete
            7. Click on Delete on Confirm popup
        @expected:
            All products has search key are removed from table
        """
        self.delete_multiple_products = DeleteProduct()
        self.delete_multiple_products.delete_multi_products(search_id)
        self.delete_multiple_products.verify_deleted_products_not_show_on_table()
        self.logout_page = LogoutPage()
        self.logout_page.logout()

    def test_tc006_verify_cannot_add_product_with_existed_ID_function(self):
        """
        @author: tu.le                         date: Feb-22-2018
        @updated:                         date:
        @summary: Verify that user cannot create a Product with ID is same with existed product
        @precondition: None
        @steps:
            1. Open page: http://portal-uat.tap.finance/merchant/
            2. Login with valid username/password of Merchant
            3. Click on Product tab
            4. Click on 'Create new product' button
            5. Add ID which is used for existed product

        @expected:
            Error message "This ID is already existed. Please enter another!!!" displays
        """
        self.add_product_existed_ID = AddProduct()
        self.add_product_existed_ID.add_product_with_existed_ID()
        self.add_product_existed_ID.verify_user_cannot_add_product_with_existed_ID()
        self.logout_page = LogoutPage()
        self.logout_page.logout()

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