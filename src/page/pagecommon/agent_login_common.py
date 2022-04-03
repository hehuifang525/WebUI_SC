"""
@author: QianJingjing
@file:   agent_login_common.py
@desc:  【登录 root 账户；登录 testbed 账户】
@step：  
"""
import time

from src.page.agent.agent_login_page import AgentLoginPage


class AgentLoginCommon(AgentLoginPage):
    # root 服务人员登录系统
    def agentlogincommon(self):
        username = "root@localhost"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)

    # testbed 服务人员登录系统
    def agentlogincommonforbed(self):
        username = "guan"
        password = '123456'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)

    def customerlogincommonforbed2(self):
        username = "李林"
        password = 'lilin'

        # 声明LoginAgent类对象，调用封装好的登陆方法
        self.send_keys(self.username_loc, username)
        self.send_keys(self.pw_loc, password)
        self.clickButton(self.submit_loc)
        time.sleep(5)