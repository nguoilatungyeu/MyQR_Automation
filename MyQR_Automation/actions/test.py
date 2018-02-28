from selenium import webdriver
from selenium.webdriver.common.by import By
from common.portal_constant import *
from selenium.webdriver.common.keys import Keys
from actions.action_login_page import *


"""class AddProduct():
    def __init__(self):
        self.login_page = LoginPage()
        self.login_page.login(CoreMerchantUserName, CoreMerchantPassword)

    def add_new_valid_product(self, id, name, details, size,image):
        self.id = id
        self.name = name
        self.details = details
        self.size = size
        self.image = image"""

class SearchProduct(Get):
   def search_product(self,id):
        #click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        #enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)

    def

        self.driver.implicitly_wait(10)
        #show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        #to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        #to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        #for
        for index in range(1,len(self.rows_table)):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW %str(index))
            if id in dynamic_row.text:
                continue
            else:
                print ("Search function fail")
                return





class DeleteProduct(Get):
    """def check_product_byID_not_exist(self,id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1, len(self.rows_table) + 1):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            if id not in dynamic_row.text:
                continue
            else:
                print("Found product with ID:", dynamic_row.text)
                return (1)"""

    def delete_first_product(self):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        # get ID of first product
        first_id = self.driver.find_element_by_xpath(TABLE_FIRST_ID)
        first_id_text = first_id.text
        # click first checkbox
        first_checkbox = self.driver.find_element_by_xpath(TABLE_FIRST_CHECKBOX)
        first_checkbox.click()
        # click Delete in Action dropdown
        action_dropdown = self.driver.find_element_by_xpath(HOME_ACTION_DROPDOWN_XPATH)
        action_dropdown.click()
        delete_dropdown = self.driver.find_element_by_xpath(HOME_DELETE_DROPDOWN_XPATH)
        delete_dropdown.click()
        # click Delete button on Confirm popup
        delete_button = self.driver.find_element_by_xpath(HOME_DELETE_BUTTON_POPUP_XPATH)
        delete_button.click()
        print("test:", first_id_text)
        return (first_id_text)

    def verify_deleted_product_not_show_on_table(self,deleted_product_id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1, len(self.rows_table) + 1):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            if deleted_product_id not in dynamic_row.text:
                continue
            else:
                print("Failed:", dynamic_row.text)

####################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.portal_constant import *
from selenium.webdriver.common.keys import Keys
from actions.action_login_page import *


"""class AddProduct():
    def __init__(self):
        self.login_page = LoginPage()
        self.login_page.login(CoreMerchantUserName, CoreMerchantPassword)

    def add_new_valid_product(self, id, name, details, size,image):
        self.id = id
        self.name = name
        self.details = details
        self.size = size
        self.image = image"""

class SearchProduct(Get):
   def search_product(self,id):
        #click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        #enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)

    def verify_search_result_table_show_only_correct_records (self, id):
        #show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        #to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        #to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        #for
        for index in range(1,len(self.rows_table)):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW %str(index))
            if id in dynamic_row.text:
                continue
            else:
                print ("Search function fail")
                return





"""class DeleteProduct(Get):
    zdef check_product_byID_not_exist(self,id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1, len(self.rows_table) + 1):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            if id not in dynamic_row.text:
                continue
            else:
                print("Found product with ID:", dynamic_row.text)
                return (1)

    def delete_first_product(self):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        # get ID of first product
        first_id = self.driver.find_element_by_xpath(TABLE_FIRST_ID)
        first_id_text = first_id.text
        # click first checkbox
        first_checkbox = self.driver.find_element_by_xpath(TABLE_FIRST_CHECKBOX)
        first_checkbox.click()
        # click Delete in Action dropdown
        action_dropdown = self.driver.find_element_by_xpath(HOME_ACTION_DROPDOWN_XPATH)
        action_dropdown.click()
        delete_dropdown = self.driver.find_element_by_xpath(HOME_DELETE_DROPDOWN_XPATH)
        delete_dropdown.click()
        # click Delete button on Confirm popup
        delete_button = self.driver.find_element_by_xpath(HOME_DELETE_BUTTON_POPUP_XPATH)
        delete_button.click()
        print("test:", first_id_text)
        return (first_id_text)

    def verify_deleted_product_not_show_on_table(self,deleted_product_id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # to lacate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to lacate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1, len(self.rows_table) + 1):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            if deleted_product_id not in dynamic_row.text:
                continue
            else:
                print("Failed:", dynamic_row.text)"""































































