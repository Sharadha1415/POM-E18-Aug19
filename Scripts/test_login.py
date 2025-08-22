'''
STEP 3  :   Written test_script for Register class present in register.py
'''

# from POM.login import Login
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email('vamsi@gmail.com')
#     login_obj.enter_login_pwd('vamsi@12345')
#
# ########################################################################
'''
STEP3 only  :   Same as Previous step, but here we are reading the test_data from the excel file.
                We are importing the excel_data function from the excel_utility file and reading the test_data.
                We are implementing the test_data in our test_scripts

'''

# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# login_d = excel_data('login')
# print(login_d)      ## {'login_email': 'vamsi@gmail.com', 'login_pwd': 'vamsi@12345'}
#
# '''
# login_d['login_email'] = 'vamsi@gmail.com'
# login_d['login_pwd'] = 'vamsi@12345'
# '''
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email(login_d['login_email'])
#     login_obj.enter_login_pwd(login_d['login_pwd'])

# ########################################################################
'''
STEP3 only
'''

# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# login_d = excel_data('login')
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email(login_d['login_email'])
#     login_obj.enter_login_pwd(login_d['login_pwd'])


# ########################################################################

'''
STEP4   :   The code for initialization of driver and launching of the web-application is given here only.
'''

# from selenium import webdriver
#
# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# login_d = excel_data('login')
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email(login_d['login_email'])
#     login_obj.enter_login_pwd(login_d['login_pwd'])
#

########################################################################
'''
STEP5   :   We are giving driver as a parameter for the Login class while creating the object.

'''
# from selenium import webdriver
#
# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
# driver.get('https://demowebshop.tricentis.com/')
#
# login_d = excel_data('login')
#
# def test_login():
#     login_obj = Login(driver)
#     login_obj.click_on_login()
#     login_obj.enter_login_email(login_d['login_email'])
#     login_obj.enter_login_pwd(login_d['login_pwd'])
#

########################################################################
'''
STEP5   :   We are defining the fixture
            The fixture includes
                *   initialization of driver object
                *   launching of the web-application
                *   yield driver 
                *   closing the driver 
            
            We are passing the fixture as a parameter for the test_function and giving it as a value for Login class

'''

# import pytest
# from selenium import webdriver
#
# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def browser_setup():
#     driver = webdriver.Chrome(opts)
#     driver.implicitly_wait(10)
#     driver.get('https://demowebshop.tricentis.com/')
#     yield driver
#     driver.close()
#
# login_d = excel_data('login')
#
# def test_login(browser_setup):
#     login_obj = Login(browser_setup)
#     login_obj.click_on_login()
#     login_obj.enter_login_email(login_d['login_email'])
#     login_obj.enter_login_pwd(login_d['login_pwd'])


########################################################################
'''
STEP5   :   We removed the fixture in test_file and gave it in conftest 
FINAL STEP IN test_login.py
'''

from POM.login import Login
from generic_utilities.excel_utility import excel_data

login_d = excel_data('login')

def test_login(browser_setup):
    login_obj = Login(browser_setup)
    login_obj.click_on_login()
    login_obj.enter_login_email(login_d['login_email'])
    login_obj.enter_login_pwd(login_d['login_pwd'])

















