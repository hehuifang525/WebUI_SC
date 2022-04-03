"""
@author: testing
@file:   menusetting_common.py
@desc:  【菜单权限管理】
@step：
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.menuset_page import MenusetPage
from src.page.agent.role_page import RolePage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.role_common import RoleCommon
from src.page.pagecommon.customer_user_commom import CustomerUserCommon
from src.page.agent.customer_user_page import CustomerUserPage


class MenusetCommon(RolePage):

    # 创建有效菜单权限管理(只填写必填项)
    def menurequiredcommon(self, agent=True):

        EntranceAgentPage(self.driver).enter_menuset()  # 系统管理--菜单权限管理
        time.sleep(8)
        MenusetPage(self.driver).addmenu()  # 点击新增按钮

        now_time = GetTimeCommon(self.driver).get_time()
        menuname = "menu必填_" + now_time

        # 权限标志、权限名称
        MenusetPage(self.driver).permission(menuname)
        MenusetPage(self.driver).menuname(menuname)
        if agent:
            MenusetPage(self.driver).chosetypeagent()
        else:
            MenusetPage(self.driver).chosetypeustomer()
        # 提交
        MenusetPage(self.driver).submit()

        return menuname

    # 创建有效菜单权限管理(只填写必填项)，无提交按钮
    def menurequiredcommon2(self, agent=True):

        EntranceAgentPage(self.driver).enter_menuset()  # 系统管理--菜单权限管理
        time.sleep(4)
        MenusetPage(self.driver).addmenu()  # 点击新增按钮

        now_time = GetTimeCommon(self.driver).get_time()
        menuname = "menu必填_" + now_time

        # 权限标志、权限名称
        MenusetPage(self.driver).permission(menuname)
        MenusetPage(self.driver).menuname(menuname)
        if agent:
            MenusetPage(self.driver).chosetypeagent()
        else:
            MenusetPage(self.driver).chosetypeustomer()
        # 提交
        # MenusetPage(self.driver).submit()
        return menuname

    # 创建无效菜单权限管理(只填写必填项)
    def menuinvalidcommon(self):
        EntranceAgentPage(self.driver).enter_menuset()  # 系统管理--菜单权限管理
        time.sleep(8)
        MenusetPage(self.driver).addmenu()  # 点击新增按钮

        now_time = GetTimeCommon(self.driver).get_time()
        menuname = "menu无效菜单权限_" + now_time

        # 权限标志、权限名称
        MenusetPage(self.driver).permission(menuname)
        MenusetPage(self.driver).menuname(menuname)

        # 无效
        RolePage(self.driver).clickchooseinvalid()
        # RolePage(self.driver).chooseinvalid()  #0716修改

        # 提交
        MenusetPage(self.driver).submit()

        return menuname

    # 编辑菜单权限取值
    def getmenuvalue(self, agent=True):
        name = MenusetPage(self.driver).getname()
        parentper = MenusetPage(self.driver).getparentper()
        type1 = MenusetPage(self.driver).gettype()
        common = MenusetPage(self.driver).getcommon()
        valid = MenusetPage(self.driver).getvalid()
        menupermission = MenusetPage(self.driver).getmenupermission()
        if agent:
            Permission = MenusetPage(self.driver).getPermissionQueue()
        else:
            Permission = MenusetPage(self.driver).getPermissionCompany()
        menuinfo = {'name': name, 'parentper': parentper,'type1': type1, 'common': common,
                    'valid': valid, 'menupermission': menupermission, 'Permission': Permission}
        return menuinfo

    def menufullcommon(self, agent=True):
        # 创建角色
        now_time = GetTimeCommon(self.driver).get_time()
        menuname = "menu全填_" + now_time

        if agent:
            rolecompanyinfo = RoleCommon(self.driver).rolerequiredcommon()
            RolePage(self.driver).savereturnbtn()
            time.sleep(3)
            Menuinfo = MenusetCommon(self.driver).menurequiredcommon()
            time.sleep(3)
            MenusetPage(self.driver).addmenu()
            # 权限标志、权限名称
            MenusetPage(self.driver).permission(menuname)
            MenusetPage(self.driver).menuname(menuname)
            MenusetPage(self.driver).chosetypeagent()
            MenusetPage(self.driver).clickPermissionjc()
            MenusetPage(self.driver).choserole(rolecompanyinfo)
            # 备注
            MenusetPage(self.driver).sendcommon('这是备注')
            MenusetPage(self.driver).choseParent(Menuinfo)
        else:
            rolecompany = CustomerUserCommon(self.driver).Companyrequiredcommon()
            rolecompanyinfo = rolecompany[0]
            time.sleep(3)
            CustomerUserPage(self.driver).Companysub()
            time.sleep(3)
            Menuinfo = MenusetCommon(self.driver).menurequiredcommon(False)
            time.sleep(3)
            MenusetPage(self.driver).addmenu()

            # 权限标志、权限名称
            MenusetPage(self.driver).permission(menuname)
            MenusetPage(self.driver).menuname(menuname)
            # 选择客户类型
            MenusetPage(self.driver).chosetypeustomer()
            MenusetPage(self.driver).clicktikect()
            MenusetPage(self.driver).choseCompany(rolecompanyinfo)
            # 备注
            MenusetPage(self.driver).sendcommon('这是备注客户')
            MenusetPage(self.driver).choseParent(Menuinfo)

        # 提交
        MenusetPage(self.driver).submit()
        time.sleep(3)
        menufullinfo = {'menuname': menuname, 'MenuParent': Menuinfo, 'rolecompay': rolecompanyinfo}
        return menufullinfo

