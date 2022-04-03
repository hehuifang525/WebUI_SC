"""
@author: QianJingjing
@file:   basecase_user.py
@desc:  【】
@step：  
"""
import time

import unittest2

from common.base import Base
from common.browser_engine1 import BrowserEngine1, BrowserEngine11
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.pagecommon.agent_login_common import AgentLoginCommon


class BaseCaseUser(unittest2.TestCase):
    def setUp(cls):
        browser = BrowserEngine1(cls)
        cls.driver = browser.open_agentbrowser()

        AgentLoginCommon(cls.driver).agentlogincommon()  # 登录root
        time.sleep(9)
        Base(cls.driver).wait(10)  # 隐式等待


    def tearDown(cls):
        # 服务人员退出系统
        AgentLoginPage(cls.driver).logout_button()

        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        cls.driver.quit()


class BaseCaseUserForTestBed(unittest2.TestCase):
    def setUp(cls):
        browser = BrowserEngine11(cls)
        cls.driver = browser.open_agentbrowser11()

        AgentLoginCommon(cls.driver).agentlogincommonforbed()  # 登录guan
        time.sleep(8)
        Base(cls.driver).wait(10)  # 隐式等待


    def tearDown(cls):
        # 服务人员退出系统
        AgentLoginPage(cls.driver).logout_button()

        # 清除浏览器cookies
        cls.driver.delete_all_cookies()
        cls.driver.quit()
