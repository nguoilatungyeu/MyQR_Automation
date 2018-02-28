from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from actions.action_login_page import *
from common.portal_constant import *

class AddProduct(Get):
    def delete_ID_if_existed(self,delete_id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        # search product which has ID user wants to delete
        search_product = SearchProduct()
        search_product.search_product(delete_id)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # check "There is no data to display" appears
        self.td = self.driver.find_element_by_xpath(TABLE_TD_CELL)
        if self.td.text == "There is no data to display":
            return
        # to locate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to locate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1, len(self.rows_table)+1):
            dynamic_id = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            if delete_id == dynamic_id.text:
                dynamic_checkbox = self.driver.find_element_by_xpath(TABLE_DYNAMIC_CHECKBOX %str(index))
                dynamic_checkbox.click()
                # click Delete in Action dropdown
                action_dropdown = self.driver.find_element_by_xpath(HOME_ACTION_DROPDOWN_XPATH)
                action_dropdown.click()
                delete_dropdown = self.driver.find_element_by_xpath(HOME_DELETE_DROPDOWN_XPATH)
                delete_dropdown.click()
                # click Delete button on Confirm popup
                delete_button = self.driver.find_element_by_xpath(HOME_DELETE_BUTTON_POPUP_XPATH)
                delete_button.click()
                return
            else:
                continue

    def add_new_valid_product(self):
        check_id = AddProduct()
        check_id.delete_ID_if_existed(ID)
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # click 'Create new Product' button
        create_new_product_button = self.driver.find_element_by_xpath(PRODUCTS_CREATE_NEW_PRODUCT_BUTTON_XPATH)
        create_new_product_button.click()
        self.driver.implicitly_wait(100)
        # set ID
        self.id_textbox = self.driver.find_element_by_xpath(PRODUCTS_ID_TEXTBOX_XPATH)
        self.id_textbox.clear()
        self.id_textbox.send_keys(ID)
        # set name
        self.name_textbox = self.driver.find_element_by_xpath(PRODUCTS_NAME_TEXTBOX_XPATH)
        self.name_textbox.clear()
        self.name_textbox.send_keys(NAME)
        # set details
        self.details_textbox = self.driver.find_element_by_xpath(PRODUCT_DETAILS_TEXTBOX_XPATH)
        self.details_textbox.clear()
        self.details_textbox.send_keys(DETAILS)
        # click No size checkbox
        self.nosize_checkbox = self.driver.find_element_by_xpath(PRODUCT_NOSIZE_CHECKBOX_XPATH)
        self.nosize_checkbox.click()
        # set price
        self.price_textbox = self.driver.find_element_by_xpath(PRODUCT_PRICE_TEXTBOX_XPATH)
        self.price_textbox.clear()
        self.price_textbox.send_keys(PRICE)
        # upload image
        self.driver.find_element_by_xpath(PRODUCT_BROWSE_IMAGE_XPATH).send_keys('C:\\Users\\tu-le\\Desktop\\xm.jpg')
        # click Save
        self.driver.implicitly_wait(100)
        save_button = self.driver.find_element_by_xpath(PRODUCT_SAVE_BUTTON_XPATH)
        save_button.click()
        save_button.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(100)

    def verify_product_show_on_table_when_user_adds_valid_product(self):
        # refresh page
        self.driver.refresh()
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # get ID of first product
        first_id = self.driver.find_element_by_xpath(TABLE_FIRST_ID)
        if first_id.text == str(ID):
            print(first_id.text,"Add valid product function: PASSED")
            return
        else:
            print(first_id.text, "Add valid product function: FAILED")


    def add_product_with_existed_ID (self):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # get ID of first product
        first_id = self.driver.find_element_by_xpath(TABLE_FIRST_ID)
        # click 'Create new Product' button
        create_new_product_button = self.driver.find_element_by_xpath(PRODUCTS_CREATE_NEW_PRODUCT_BUTTON_XPATH)
        create_new_product_button.click()
        # set ID = first_id_text
        id_textbox = self.driver.find_element_by_xpath(PRODUCTS_ID_TEXTBOX_XPATH)
        id_textbox.send_keys(first_id.text)

    def verify_user_cannot_add_product_with_existed_ID(self):
        assert "This ID is already existed. Please enter another!!!" in self.driver.page_source


class SearchProduct(Get):
    def search_product(self,id):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        self.driver.implicitly_wait(10)
        # enter text(id) into search textbox and press Enter key
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.send_keys(id)
        search_textbox.send_keys(Keys.RETURN)

    def verify_search_result_table_show_only_correct_records (self,id):
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # to locate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to locate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        for index in range(1,len(self.rows_table)):
            dynamic_row = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW %str(index))
            if id in dynamic_row.text:
                continue
            else:
                print ("Search function fail")
                return

class DeleteProduct(Get):
    def delete_first_product(self):
        # get ID of first product
        first_id = self.driver.find_element_by_xpath(TABLE_FIRST_ID)
        first_id_text = first_id.text
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
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
        # print("test:", first_id_text) -> to check correct first_id_text is correct
        return (first_id_text)

    def verify_deleted_product_not_show_on_table(self,deleted_product_id):
        # search deleted Product
        self.search_product = SearchProduct()
        self.search_product.search_product(deleted_product_id)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        # check "There is no data to display" appears
        self.td = self.driver.find_element_by_xpath(TABLE_TD_CELL)
        if self.td.text == "There is no data to display":
            print (deleted_product_id,"is deleted from table")
        else:
            print ("Deleted function failed")

    def delete_multi_products(self,key_deleted):
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        # search Product with key_deleted to delete
        self.search_product = SearchProduct()
        self.search_product.search_product(key_deleted)
        # show all result rows
        page_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_XPATH)
        page_dropdown.click()
        self.driver.implicitly_wait(10)
        page_all_dropdown = self.driver.find_element_by_xpath(HOME_PAGE_DROPDOWN_ALL_XPATH)
        page_all_dropdown.click()
        ## get ID of all products in table result
        # to locate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to locate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        # for
        self.list_result = []
        for index in range(1, len(self.rows_table)+1):
            dynamic_ID = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(index))
            list_temp = [dynamic_ID.text]
            self.list_result = self.list_result + list_temp
        print("Following IDs are deleted:",self.list_result)

        # check on 'Check all' checkbox
        checkall_checkbox = self.driver.find_element_by_xpath(TABLE_CHECKALL_CHECKBOX)
        checkall_checkbox.click()
        # click Delete in Action dropdown
        action_dropdown = self.driver.find_element_by_xpath(HOME_ACTION_DROPDOWN_XPATH)
        action_dropdown.click()
        delete_dropdown = self.driver.find_element_by_xpath(HOME_DELETE_DROPDOWN_XPATH)
        delete_dropdown.click()
        # click Delete button on Confirm popup
        delete_button = self.driver.find_element_by_xpath(HOME_DELETE_BUTTON_POPUP_XPATH)
        delete_button.click()
        return self.list_result

    def verify_deleted_products_not_show_on_table(self):
        # clear search textbox
        search_textbox = self.driver.find_element_by_xpath(PRODUCTS_SEARCH_TEXTBOX_XPATH)
        search_textbox.clear()
        # click Products tab
        product_tab = self.driver.find_element_by_xpath(HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH)
        product_tab.click()
        # to locate table
        self.mytable = self.driver.find_element_by_xpath(TABLE)
        # to locate rows of table
        self.rows_table = self.mytable.find_elements_by_tag_name("tr")
        for j in range (0,len(self.list_result)):
            for i in range(1, len(self.rows_table)):
                dynamic_ID = self.driver.find_element_by_xpath(TABLE_DYNAMIC_ROW_BY_ID % str(i))
                if dynamic_ID.text in self.list_result[j]:
                     print ("Delete multi products function failed with ID:",dynamic_ID.text)
                     break
                else:
                    print("Checked that",dynamic_ID.text," is deleted")











































