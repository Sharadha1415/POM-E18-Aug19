import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://demowebshop.tricentis.com/')

class Login:

    def click_on_login(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()

    def enter_login_email(self, email_id):
        driver.find_element('id', 'Email').send_keys(email_id)

    def enter_login_pwd(self, pwd):
        driver.find_element('id', 'Password').send_keys(pwd)

login_obj = Login()
login_obj.click_on_login()
login_obj.enter_login_email('vamsi@gmail.com')
login_obj.enter_login_pwd('vamsi@12345')










