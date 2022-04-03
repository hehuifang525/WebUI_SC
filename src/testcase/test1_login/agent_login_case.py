# coding=utf-8
"""
@author: QianJingjing
@file:   agent_login_case.py
@desc:  【登录 user 界面检查】
@step：  1. 检查正确的登录名、密码
         2. 正确的登录名、错误的密码登录会提示“登录失败！用户名或密码错误。”
"""

import time

import unittest2

from common.base import Base
from common.browser_engine1 import BrowserEngine1
from src.page.agent.agent_login_page import AgentLoginPage


class AgentLogin(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化
        browser = BrowserEngine1(cls)
        # 调方法
        cls.driver = browser.open_agentbrowser()
        Base(cls.driver).wait(5)  # 隐式等待

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        time.sleep(3)
        cls.driver.quit()

    # 这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里

    def test_1_loginSuccess(self):
        username = "root@localhost"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        AgentLoginPage(self.driver).input_username(username)
        AgentLoginPage(self.driver).input_passwd(password)
        AgentLoginPage(self.driver).login_button()
        time.sleep(7)

        # 检查是否正常登录系统
        # a检查页面 urltitle
        # hope = u'主页'
        # result = Base(self.driver).get_title()
        # 0731 修改登录成功判断方法
        result = self.driver.find_element_by_id('logout').text
        self.assertEqual(result, '退出', msg='系统未正常登录')

        # # b获取 主页 “您已登录为 OTRSAdmin” 文本信息
        # result = AgentLoginPage(self.driver).login_usermessage()
        # hope = u"( 您已登录为 OTRSAdmin )"
        # self.assertEqual(result, hope, "登录失败")
        # # 判断是否登陆成功
        # try:
        #     self.assertEqual(result,hope)
        # except AssertionError as e:
        #     print("Test Fail：未正确登录root账户，登录人在主页显示不正确")
        # print('成功登录')
        # 退出系统
        time.sleep(5)
        AgentLoginPage(self.driver).logout_button()

    # @unittest2.skip("跳过已知问题用例")
    # @unittest2.expectedFailure
    def test_2_loginFailed(self):
        username = "root@localhost"
        password = '1234567'
        AgentLoginPage(self.driver).input_username(username)
        AgentLoginPage(self.driver).input_passwd(password)
        AgentLoginPage(self.driver).login_button()
        time.sleep(1)
        login_failpw_message = AgentLoginPage(self.driver).failedpw_message()
        # print(login_failpw_message)
        self.assertEqual(login_failpw_message, u"登录失败！用户名或密码错误。")

        # try:
        #     self.assertEqual(login_failpw_message, u"登录失败！用户名或密码错误。")
        # except AssertionError as e:
        #     print("测试失败")
