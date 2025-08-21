## STEP 3

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
#
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
#
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
#
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

from selenium import webdriver

from POM.register import Register
from generic_utilities.excel_utility import excel_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://demowebshop.tricentis.com/')

reg_d = excel_data('reg')

def test_reg():
    reg_obj = Register(driver)
    reg_obj.click_on_register()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname(reg_d['fname'])
    reg_obj.enter_lastname(reg_d['lname'])
    reg_obj.enter_reg_email(reg_d['reg_email'])
    reg_obj.enter_reg_pwd(reg_d['pwd'])
    reg_obj.enter_confirm_pwd(reg_d['confirm_pwd'])




















