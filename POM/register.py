import time

# ## STEP1
#
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
STEP2
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
STEP3
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
STEP4
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
STEP4
'''

class Register:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome(opts)

    def click_on_register(self):
        self.driver.find_element('xpath', '//a[@class="ico-register"]').click()

    def click_on_gender_btn(self):
        self.driver.find_element('id', 'gender-male').click()

    def enter_firstname(self, fname):
        self.driver.find_element('id', 'FirstName').send_keys(fname)

    def enter_lastname(self, lname):
        self.driver.find_element('id', 'LastName').send_keys(lname)

    def enter_reg_email(self, email_id):
        self.driver.find_element('id', 'Email').send_keys(email_id)

    def enter_reg_pwd(self, pwd):
        self.driver.find_element('id', 'Password').send_keys(pwd)

    def enter_confirm_pwd(self, confirm_pwd):
        self.driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)























