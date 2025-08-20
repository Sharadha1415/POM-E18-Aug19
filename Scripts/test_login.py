from POM.login import Login

def test_login():
    login_obj = Login()
    login_obj.click_on_login()
    login_obj.enter_login_email('vamsi@gmail.com')
    login_obj.enter_login_pwd('vamsi@12345')

