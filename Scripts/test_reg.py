'''
STEP 3  :   Written test_script for Register class present in register.py
'''

# from POM.register import Register
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Vamsi Adithya')
#     reg_obj.enter_lastname('Narayan')
#     reg_obj.enter_reg_email('vamsi@gmail.com')
#     reg_obj.enter_reg_pwd('vamsi@12345')
#     reg_obj.enter_confirm_pwd('vamsi@12345')

# ############################################################################

'''
STEP3 only  :   Same as Previous step, but here we are reading the test_data from the excel file.
                We are importing the excel_data function from the excel_utility file and reading the test_data.
                We are implementing the test_data in our test_scripts

'''

# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# reg_d = excel_data('reg')
# print(reg_d)
#
# '''
# {'fname': 'Vamsi Adithya', 'lname': 'Narayan', 'reg_email': 'vamsi@gmail.com', 'pwd': 'vamsi@12345', 'confirm_pwd': 'vamsi@12345'}
#
# reg_d['fname'] = 'Vamsi Adithya'
# reg_d['lname'] = 'Narayan'
# reg_d['reg_email'] = 'vamsi@gmail.com'
# reg_d['pwd'] = 'vamsi@12345'
# reg_d['confirm_pwd'] = 'vamsi@12345'
#
# '''
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(reg_d['fname'])
#     reg_obj.enter_lastname(reg_d['lname'])
#     reg_obj.enter_reg_email(reg_d['reg_email'])
#     reg_obj.enter_reg_pwd(reg_d['pwd'])
#     reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])


# ############################################################################

'''
STEP3 only
'''

# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# reg_d = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(reg_d['fname'])
#     reg_obj.enter_lastname(reg_d['lname'])
#     reg_obj.enter_reg_email(reg_d['reg_email'])
#     reg_obj.enter_reg_pwd(reg_d['pwd'])
#     reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])

# ############################################################################

'''
STEP4   :   The code for initialization of driver and launching of the web-application is given here only.
'''

# from selenium import webdriver
#
# from POM.register import Register
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
# reg_d = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(reg_d['fname'])
#     reg_obj.enter_lastname(reg_d['lname'])
#     reg_obj.enter_reg_email(reg_d['reg_email'])
#     reg_obj.enter_reg_pwd(reg_d['pwd'])
#     reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])


############################################################################

'''
STEP5   :   We are giving driver as a parameter for the Register class while creating the object.

'''

# from selenium import webdriver
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
# driver.get('https://demowebshop.tricentis.com/')
#
#
# reg_d = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register(driver)
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(reg_d['fname'])
#     reg_obj.enter_lastname(reg_d['lname'])
#     reg_obj.enter_reg_email(reg_d['reg_email'])
#     reg_obj.enter_reg_pwd(reg_d['pwd'])
#     reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])

############################################################################

'''
STEP5   :   We are defining the fixture
            The fixture includes
                *   initialization of driver object
                *   launching of the web-application
                *   yield driver 
                *   closing the driver 
            
            We are passing the fixture as a parameter for the test_function and giving it as a value for Register class

'''
# import pytest
# from selenium import webdriver
#
# from POM.register import Register
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
# reg_d = excel_data('reg')
#
# ## browser_setup --> driver
#
# def test_reg(browser_setup):
#     reg_obj = Register(browser_setup)
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(reg_d['fname'])
#     reg_obj.enter_lastname(reg_d['lname'])
#     reg_obj.enter_reg_email(reg_d['reg_email'])
#     reg_obj.enter_reg_pwd(reg_d['pwd'])
#     reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])


############################################################################

'''
STEP5   :   We removed the fixture in test_file and gave it in conftest 
FINAL STEP in test_reg.py
'''

from POM.register import Register
from generic_utilities.excel_utility import excel_data

reg_d = excel_data('reg')

def test_reg(browser_setup):
    reg_obj = Register(browser_setup)
    reg_obj.click_on_register()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname(reg_d['fname'])
    reg_obj.enter_lastname(reg_d['lname'])
    reg_obj.enter_reg_email(reg_d['reg_email'])
    reg_obj.enter_reg_pwd(reg_d['pwd'])
    reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])

















