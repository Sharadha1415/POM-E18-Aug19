# from POM.login import Login
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email('vamsi@gmail.com')
#     login_obj.enter_login_pwd('vamsi@12345')
#
# ########################################################################
#
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
#
#
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
#
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

from selenium import webdriver

from POM.login import Login
from generic_utilities.excel_utility import excel_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://demowebshop.tricentis.com/')

login_d = excel_data('login')

def test_login():
    login_obj = Login(driver)
    login_obj.click_on_login()
    login_obj.enter_login_email(login_d['login_email'])
    login_obj.enter_login_pwd(login_d['login_pwd'])




















