"""
@author: DT_testing
@file:   customer_login_page.py
@desc:  【用户登录】
@step：  
"""

from common.base import Base
from selenium.webdriver.common.by import By


#继承BasePage类
class CustomerLoginPage(Base):

    '''
    page
    '''
    username_loc = (By.CSS_SELECTOR, '[formcontrolname="User"]')
    pw_loc = (By.CSS_SELECTOR, '[formcontrolname ="Password"]')
    # submit_loc = (By.CLASS_NAME, 'login-form-button')
    submit_loc = (By.ID, 'submit')
    # message_loc = (By.ID, 'translate')
    logout_loc = (By.ID, 'logout')
    failedpw_message_loc = (By.XPATH, '/html/body/app-root/customer-root/nz-layout/customer-login/div/div/div[1]/nz-alert/div/span')

    '''
    flow
    '''
    # 操作：输入用户名操作、输入密码操作、点击登陆按钮操作
    def input_username(self, username):
        self.send_keys(self.username_loc, username)

    def input_passwd(self, password):
        # self.find_element(self.pw_loc).send_keys(password)
        self.send_keys(self.pw_loc, password)

    def login_button(self):
        self.clickButton(self.submit_loc)

    # 查看登录信息（登录成功页面中查看已登录的账号）
    # def login_usermessage(self):
    #     return self.find_element(self.message_loc).text

    # 退出系统
    def logout_button(self):
        self.clickButton(self.logout_loc)

    # 用户名或密码不合理时页面提示信息
    def failedpw_message(self):
        return self.find_element(self.failedpw_message_loc).text

