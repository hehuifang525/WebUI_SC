"""
@author: QianJingjing
@file:   role_common.py
@desc:  【创建必填值填写的角色 及 全部填写字段的角色】
@step：  都是服务人员页面内部的值填写
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.role_page import RolePage
from src.page.pagecommon.get_time_common import GetTimeCommon


class RoleCommon(RolePage):

    # 创建有效角色(只填写必填项)
    def rolerequiredcommon(self):

        EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
        time.sleep(10)
        RolePage(self.driver).addrole()  # 点击新增按钮

        now_time = GetTimeCommon(self.driver).get_time()
        name = "role必填项_" + now_time

        RolePage(self.driver).rolename(name)
        return name

    # 创建无效角色(只填写必填项)
    def roleinvalidcommon(self):
        EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
        time.sleep(10)
        RolePage(self.driver).addrole()  # 点击新增按钮

        now_time = GetTimeCommon(self.driver).get_time()
        name = "无效角色_" + now_time

        RolePage(self.driver).rolename(name)
        # 无效
        RolePage(self.driver).clickchooseinvalid()
        #RolePage(self.driver).chooseinvalid()
        return name

    # 创建角色(全部填写值，父角色是 Postmaster)
    def rolefullcommon(self):
        EntranceAgentPage(self.driver).enter_role()  # 开始--角色
        time.sleep(10)
        RolePage(self.driver).addrole()  # 点击新增按钮
        # 填写name
        now_time = GetTimeCommon(self.driver).get_time()
        name = "角色全填test_" + now_time
        RolePage(self.driver).rolename(name)
        # 父角色
        parentrole = "Postmaster"
        RolePage(self.driver).parentrole(parentrole)
        RolePage(self.driver).chooseparentrole(parentrole)

        # 系统邮件地址
        RolePage(self.driver).systemadress()
        RolePage(self.driver).choosesystemadress()

        # 备注
        RolePage(self.driver).comment("备注信息" + name)

        # 所有者、负责人、组管理者（调用agent）
        return name
