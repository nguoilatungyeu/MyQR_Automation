#Login screen
LOGIN_USERNAME_INPUT_XPATH = "//input[@name='username']"
LOGIN_PASSWORD_INPUT_XPATH = "//input[@name='password']"
LOGIN_SIGNIN_BUTTON_XPATH = "//input[@value='Login']"

#Home screen
HOME_LOGOUT_LINK_XPATH = "//a[contains(@href,'logout')]"
HOME_ACCOUNT_DROPDOWN_XPATH = "//div[@data-toggle='dropdown']"
HOME_ORDERS_SHOP_ADMIN_TAB_XPATH = "//a[@href='#/shop/orders']"
HOME_PRODUCTS_MERCHANT_ADMIN_TAB_XPATH = "//ul[@id='menu-content']/li/a"
HOME_PAGE_DROPDOWN_XPATH = "//button[@id='pageDropDown']"
HOME_PAGE_DROPDOWN_ALL_XPATH = "//a[text()='All']"
HOME_ACTION_DROPDOWN_XPATH ="//button[@data-toggle='dropdown']"
HOME_DELETE_DROPDOWN_XPATH = "//a[text()='Delete']"
HOME_DELETE_BUTTON_POPUP_XPATH = "//button[@class='btn-delete']"

#Merchat creates new product
PRODUCTS_SEARCH_TEXTBOX_XPATH = "//input[@placeholder='Search']"
PRODUCTS_CREATE_NEW_PRODUCT_BUTTON_XPATH = "//button[@class='btn btn-default']"
PRODUCTS_ID_TEXTBOX_XPATH = "//input[@name='code']"
PRODUCTS_SAME_ID_ERROR_XPATH = "//p[contains(.,'This ID is already existed. Please enter another!!!')]"
PRODUCTS_NAME_TEXTBOX_XPATH = "//div/input[@name='name']"
PRODUCT_DETAILS_TEXTBOX_XPATH = "//textarea[@name='description']"
PRODUCT_NOSIZE_CHECKBOX_XPATH = "//div[@id = 'create-product-dialog']//input[@type='checkbox']"
PRODUCT_PRICE_TEXTBOX_XPATH = "//div[@id = 'create-product-dialog']//input[@name='noSizeInput']"
PRODUCT_BROWSE_IMAGE_XPATH = "//input[@accept = 'image/*']"
PRODUCT_SAVE_BUTTON_XPATH = "//div[@id = 'create-product-dialog']//button[@class='btn-save']"



#Table
TABLE_GET_ROW = "//table[@class='table table-bordered']//tr[index]"
TABLE = "//table[@class='table table-bordered']//tbody"
TABLE_ROW = "//table[@class='table table-bordered']//tbody/tr"

test = "//table[@class='table table-bordered']//tr[1]"
TABLE_DYNAMIC_ROW = "//table[@class='table table-bordered']//tr[%s]" # dynamic interface
TABLE_DYNAMIC_ROW_BY_ID = "//table[@class='table table-bordered']//tr[%s]/td[2]"
TABLE_FIRST_CHECKBOX = "//table[@class='table table-bordered']//tr[1]/td[1]/input"
TABLE_DYNAMIC_CHECKBOX = "//table[@class='table table-bordered']//tr[%s]/td[1]/input"
TABLE_FIRST_ID = "//table[@class='table table-bordered']//tr[1]/td[2]"
TABLE_TD_CELL = "//td"
TABLE_CHECKALL_CHECKBOX = "//input[@id='checkboxAll']"

#Browser
Browser_Firefox = "Firefox"
Browser_IE = "IE"
Browser_Chrome = "Chrome"
Browser_Safari = "Safari"

#Account Login
CoreMerchantUserName = "admin@merchant"
CoreMerchantPassword = "123123"

CoreShopUserName = "admin@shop"
CoreShopPassword = "123123"

#URL
url1 =  "http://portal-uat.tap.finance/merchant/"

#search text
search_id = "test"

#data to create new product
ID = "testID2"
NAME = "Hunter1"
DETAILS = "Shoes for running"
PRICE = "4000"

class DataUser (object):
    def __init__(self,id, name, details, price):
        self.id = id
        self.name = name
        self.details = details
        self.price = price

    def generate_data (self):
        self.id =


