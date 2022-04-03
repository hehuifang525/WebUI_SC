"""
@author: QianJingjing
@file:   basecase_customer.py
@desc:  【】
@step：  
"""
import unittest2

from common.base import Base
from common.browser_engine2 import BrowserEngine22, BrowserEngine2
from src.page.customer.customer_login_page import CustomerLoginPage
from src.page.pagecommon.customer_login_common import CustomerLoginCommon


class BaseCaseCustomer(unittest2.TestCase):

    def setUp(cls):
        browser = BrowserEngine2(cls)
        cls.driver = browser.open_customerbrowser()

        Base(cls.driver).wait(6)  # 隐式等待

    def tearDown(cls):
        # 用户退出系统
        # AgentLoginPage(cls.driver).logout_button()

        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        cls.driver.quit()

# 登录用户：鲁班
class BaseCaseCustomerForTestBed(unittest2.TestCase):
    def setUp(cls):
        browser = BrowserEngine22(cls)
        cls.driver = browser.open_customerbrowser22()

        CustomerLoginCommon(cls.driver).customerlogincommonforbed()  # 登录 鲁班
        # time.sleep(8)
        Base(cls.driver).wait(10)  # 隐式等待

    def tearDown(cls):
        #  用户退出系统
        CustomerLoginPage(cls.driver).logout_button()

        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        cls.driver.quit()

# 登录用户：A-1
class BaseCaseCustomerForTestBed2(unittest2.TestCase):
    def setUp(cls):
        browser = BrowserEngine22(cls)
        cls.driver = browser.open_customerbrowser22()

        CustomerLoginCommon(cls.driver).customerlogincommonforbed2()  # 登录 A-1
        # time.sleep(8)
        Base(cls.driver).wait(10)  # 隐式等待

    def tearDown(cls):
        #  用户退出系统
        CustomerLoginPage(cls.driver).logout_button()

        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        cls.driver.quit()