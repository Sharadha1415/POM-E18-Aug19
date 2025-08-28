import time

'''
STEP1   :   In https://demowebshop.tricentis.com/, we are clicking on register and filling the register data
            execute this file only
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('xpath', '//a[@class="ico-register"]').click()
# driver.find_element('id', 'gender-male').click()
# driver.find_element('id', 'FirstName').send_keys('Vamsi Adithya')
# driver.find_element('id', 'LastName').send_keys('Narayan')
# driver.find_element('id', 'Email').send_keys('vamsi@gmail.com')
# driver.find_element('id', 'Password').send_keys('vamsi@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('vamsi@12345')

##############################################################################

'''
STEP2   :   We defined class(attributes) for the automation script.
            Here only we are creating the object and calling the attributes
            This step execution is happening here only
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[@class="ico-register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#
#
# reg_obj = Register()
# reg_obj.click_on_register()
# reg_obj.click_on_gender_btn()
# reg_obj.enter_firstname('Vamsi Adithya')
# reg_obj.enter_lastname('Narayan')
# reg_obj.enter_reg_email('vamsi@gmail.com')
# reg_obj.enter_reg_pwd('vamsi@12345')
# reg_obj.enter_confirm_pwd('vamsi@12345')


##############################################################################

'''
STEP3   :   We removed the reg_obj and calling the attributes and gave it in test_file.
            In this file only Register class and its attributes are present.
            Object creation and calling the attributes is present in test_reg.py
            Execution happens in test_reg.py 
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[@class="ico-register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)

##############################################################################

'''
STEP4   :   We removed initialization of driver and launching of the web-application and gave it in test_reg.py 
            Execution in test_reg.py
'''

# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[@class="ico-register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#
# ## ERROR
# ## There is no driver object


##############################################################################

'''
STEP5   :   We defined __init__ and we are giving driver as a parameter.
            So, self.driver --> driver = webdriver.Chrome()
            
            We will replace driver with self.driver
            
            Execution in test_reg.py
'''

# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome(opts)
#
#     def click_on_register(self):
#         self.driver.find_element('xpath', '//a[@class="ico-register"]').click()
#
#     def click_on_gender_btn(self):
#         self.driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         self.driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         self.driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         self.driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)

##############################################################################

'''
STEP6   :   We stored locator name and locator value in a object_repository.
            We are replacing the loactor name and locator value with the specified variable name

'''

# from object_repository.reg_repo import RegisterLocators
#
# reg_l = RegisterLocators()
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver  ## self.driver --> driver = webdriver.Chrome(opts)
#
#     def click_on_register(self):
#         # self.driver.find_element('xpath', '//a[@class="ico-register"]').click()
#         self.driver.find_element(*reg_l.reg_link).click()
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element('id', 'gender-male').click()
#         self.driver.find_element(*reg_l.gender_btn).click()
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element('id', 'FirstName').send_keys(fname)
#         self.driver.find_element(*reg_l.firstname).send_keys(fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element('id', 'LastName').send_keys(lname)
#         self.driver.find_element(*reg_l.lastname).send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         # self.driver.find_element('id', 'Email').send_keys(email_id)
#         self.driver.find_element(*reg_l.reg_email).send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         # self.driver.find_element('id', 'Password').send_keys(pwd)
#         self.driver.find_element(*reg_l.reg_pwd).send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         # self.driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#         self.driver.find_element(*reg_l.confirm_pwd).send_keys(confirm_pwd)

##############################################################################

'''
STEP6 only. Removed all the commented lines

'''

# from object_repository.reg_repo import RegisterLocators
#
# reg_l = RegisterLocators()
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver  ## self.driver --> driver = webdriver.Chrome(opts)
#
#     def click_on_register(self):
#         self.driver.find_element(*reg_l.reg_link).click()
#
#     def click_on_gender_btn(self):
#         self.driver.find_element(*reg_l.gender_btn).click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element(*reg_l.firstname).send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element(*reg_l.lastname).send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         self.driver.find_element(*reg_l.reg_email).send_keys(email_id)
#
#     def enter_reg_pwd(self, pwd):
#         self.driver.find_element(*reg_l.reg_pwd).send_keys(pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         self.driver.find_element(*reg_l.confirm_pwd).send_keys(confirm_pwd)

#
# ##############################################################################

'''
STEP7   :   Created SeleniumWrapper class.
            Storing the web-element methods inside the SeleniumWrapper class

'''
#
# from object_repository.reg_repo import RegisterLocators
#
# reg_l = RegisterLocators()
#
# class SeleniumWrapper:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_on_element(self, var_name):
#         self.driver.find_element(*var_name).click()
#
#     def enter_data(self, var_name, data):
#         self.driver.find_element(*var_name).send_keys(data)
#
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver  ## self.driver --> driver = webdriver.Chrome(opts)
#         self.sel = SeleniumWrapper(driver)
#
#     def click_on_register(self):
#         # self.driver.find_element(*reg_l.reg_link).click()
#         self.sel.click_on_element(reg_l.reg_link)
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element(*reg_l.gender_btn).click()
#         self.sel.click_on_element(reg_l.gender_btn)
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element(*reg_l.firstname).send_keys(fname)
#         self.sel.enter_data(reg_l.firstname, fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element(*reg_l.lastname).send_keys(lname)
#         self.sel.enter_data(reg_l.lastname, lname)
#
#     def enter_reg_email(self, email_id):
#         # self.driver.find_element(*reg_l.reg_email).send_keys(email_id)
#         self.sel.enter_data(reg_l.reg_email, email_id)
#
#     def enter_reg_pwd(self, pwd):
#         # self.driver.find_element(*reg_l.reg_pwd).send_keys(pwd)
#         self.sel.enter_data(reg_l.reg_pwd, pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         # self.driver.find_element(*reg_l.confirm_pwd).send_keys(confirm_pwd)
#         self.sel.enter_data(reg_l.confirm_pwd, confirm_pwd)

#
# ##############################################################################
#
'''
STEP7 only. Removed commented lines

'''
#
# from object_repository.reg_repo import RegisterLocators
#
# reg_l = RegisterLocators()
#
# class SeleniumWrapper:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_on_element(self, var_name):
#         self.driver.find_element(*var_name).click()
#
#     def enter_data(self, var_name, data):
#         self.driver.find_element(*var_name).send_keys(data)
#
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver  ## self.driver --> driver = webdriver.Chrome(opts)
#         self.sel = SeleniumWrapper(driver)
#
#     def click_on_register(self):
#         self.sel.click_on_element(reg_l.reg_link)
#
#     def click_on_gender_btn(self):
#         self.sel.click_on_element(reg_l.gender_btn)
#
#     def enter_firstname(self, fname):
#         self.sel.enter_data(reg_l.firstname, fname)
#
#     def enter_lastname(self, lname):
#         self.sel.enter_data(reg_l.lastname, lname)
#
#     def enter_reg_email(self, email_id):
#         self.sel.enter_data(reg_l.reg_email, email_id)
#
#     def enter_reg_pwd(self, pwd):
#         self.sel.enter_data(reg_l.reg_pwd, pwd)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         self.sel.enter_data(reg_l.confirm_pwd, confirm_pwd)


##############################################################################

'''
STEP8   :   Given SeleniumWrapper in webdriver_utility and  importing it

'''

from object_repository.reg_repo import RegisterLocators
from generic_utilities.webdriver_utility import SeleniumWrapper

reg_l = RegisterLocators()

class Register:

    def __init__(self, driver):
        self.driver = driver  ## self.driver --> driver = webdriver.Chrome(opts)
        self.sel = SeleniumWrapper(driver)

    def click_on_register(self):
        self.sel.click_on_element(reg_l.reg_link)

    def click_on_gender_btn(self):
        self.sel.click_on_element(reg_l.gender_btn)

    def enter_firstname(self, fname):
        self.sel.enter_data(reg_l.firstname, fname)

    def enter_lastname(self, lname):
        self.sel.enter_data(reg_l.lastname, lname)

    def enter_reg_email(self, email_id):
        self.sel.enter_data(reg_l.reg_email, email_id)

    def enter_reg_pwd(self, pwd):
        self.sel.enter_data(reg_l.reg_pwd, pwd)

    def enter_confirm_pwd(self, confirm_pwd):
        self.sel.enter_data(reg_l.confirm_pwd, confirm_pwd)










