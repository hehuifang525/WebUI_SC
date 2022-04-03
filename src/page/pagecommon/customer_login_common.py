"""
@author: QianJingjing
@file:   customer_login_common.py
@desc:  【登录xxxxx账户；登录 testbed 用户账户】
@step：  
"""
import time
from src.page.customer.customer_login_page import CustomerLoginPage


class CustomerLoginCommon(CustomerLoginPage):
    # # xx用户登录系统
    # def customerlogincommon(self):
    #     username = "root@localhost"
    #     password = '123456'
    #
    #     # 声明LoginAgent类对象，调用封装好的登陆方法
    #     self.send_keys(self.username_loc, username)
    #     self.send_keys(self.pw_loc, password)
    #     self.clickButton(self.submit_loc)
    #     time.sleep(5)

    # testbed 用户登录系统
    def customerlogincommonforbed(self):
        username = "鲁班"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)

    def customerlogincommonforbed2(self):
        username = "A-1"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)

    def customerlogincommonforbed3(self):
        username = "A-2"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)
