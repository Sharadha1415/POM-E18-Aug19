import time

'''
STEP1   :   In https://demowebshop.tricentis.com/, we are clicking on login and filling the login data
            execute this file only
'''
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
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# driver.find_element('id', 'Email').send_keys('vamsi@gmail.com')
# driver.find_element('id', 'Password').send_keys('vamsi@12345')


# ################################################################################

'''
STEP2   :   We defined class(attributes) for the automation script.
            Here only we are creating the object and calling the attributes
            This step execution is happening here only
'''

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
#
# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
# login_obj = Login()
# login_obj.click_on_login()
# login_obj.enter_login_email('vamsi@gmail.com')
# login_obj.enter_login_pwd('vamsi@12345')

# ################################################################################
#

'''
STEP3   :   We removed the login_obj and calling the attributes and gave it in test_file.
            In this file only Login class and its attributes are present.
            Object creation and calling the attributes is present in test_login.py
            Execution happens in test_login.py 
'''
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
#
# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)

# ################################################################################
#
'''
STEP4   :   We removed initialization of driver and launching of the web-application and gave it in test_login.py 
            Execution in test_login.py
'''
#
# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)

## ERROR
## Because there is no driver

################################################################################
'''
STEP5   :   We defined __init__ and we are giving driver as a parameter.
            So, self.driver --> driver = webdriver.Chrome()

            We will replace driver with self.driver

            Execution in test_login.py
'''

# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_login(self):
#         self.driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         self.driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, pwd):
#         self.driver.find_element('id', 'Password').send_keys(pwd)

################################################################################
'''
STEP6   :   We stored locator name and locator value in a object_repository.
            We are replacing the loactor name and locator value with the specified variable name

'''

# from object_repository.login_repo import LoginLocators
#
# login_l = LoginLocators()
#
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_login(self):
#         # self.driver.find_element('xpath', '//a[text()="Log in"]').click()
#         self.driver.find_element(*login_l.login_link).click()
#
#     def enter_login_email(self, email_id):
#         # self.driver.find_element('id', 'Email').send_keys(email_id)
#         self.driver.find_element(*login_l.login_email).send_keys(email_id)
#
#     def enter_login_pwd(self, pwd):
#         # self.driver.find_element('id', 'Password').send_keys(pwd)
#         self.driver.find_element(login_l.login_pwd).send_keys(pwd)

################################################################################
'''
STEP6 only. Removed all the commented lines
'''

from object_repository.login_repo import LoginLocators

login_l = LoginLocators()

class Login:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> driver = webdriver.Chrome()

    def click_on_login(self):
        self.driver.find_element(*login_l.login_link).click()

    def enter_login_email(self, email_id):
        self.driver.find_element(*login_l.login_email).send_keys(email_id)

    def enter_login_pwd(self, pwd):
        self.driver.find_element(*login_l.login_pwd).send_keys(pwd)






































