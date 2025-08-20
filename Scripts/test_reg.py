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


############################################################################

from POM.register import Register

def test_reg():
    reg_obj = Register()
    reg_obj.click_on_register()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname('Vamsi Adithya')
    reg_obj.enter_lastname('Narayan')
    reg_obj.enter_reg_email('vamsi@gmail.com')
    reg_obj.enter_reg_pwd('vamsi@12345')
    reg_obj.enter_confirm_pwd('vamsi@12345')



























