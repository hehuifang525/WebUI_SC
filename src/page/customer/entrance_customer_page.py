"""
@author: DT_testing
@file:   entrance_customer_page.py
@desc:  【进入各个入口】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base import Base


class EntranceCustomerPage(Base):
    '''
    系统左侧方及隐藏的按钮
    '''
    # 主菜单menu
    menu_loc = (By.ID, 'submenu')
    # 合起菜单
    closemenu_loc = (By.CSS_SELECTOR, '[class="subClose"]')

    # 新建工单
    ticketcreate_loc = (By.CSS_SELECTOR, '[title="TESTBED_测试流程"]')
    ticketcreate2_loc = (By.CSS_SELECTOR, '[title="不同客户使用"]')


    # 工单搜索
    ticketsearch_loc = (By.CSS_SELECTOR, '[title="工单搜索"]')

    # 主页 ( 客户用户信息中心 )
    dashboard_loc = (By.CSS_SELECTOR, '[title="主页 ( 客户用户信息中心 )"]')


    # CMDB 概览
    cmdb_loc = (By.CSS_SELECTOR, '[title="CMDB 概览"]')

    # 服务
    service_loc = (By.CSS_SELECTOR, '[title="服务"]')

    # 知识库概览
    faq_loc = (By.CSS_SELECTOR, '[title="知识库概览"]')

    # 客户用户管理
    customer_user_loc = (By.CSS_SELECTOR, '[title="客户用户管理"]')

    # 点击开始菜单按钮
    def openmenu(self):
        self.find_element(self.menu_loc).click()
        time.sleep(2)
    # 点击关闭菜单按钮
    def closemenu(self):
        self.find_element(self.closemenu_loc).click()
        time.sleep(2)
    # 点击菜单---主页
    def enter_home(self):
        self.find_element(self.menu_loc).click()
        time.sleep(1)
        self.find_element(self.dashboard_loc).click()

    # # 点击菜单--角色
    # def enter_role(self):
    #     # 0717修改
    #     time.sleep(6)
    #     try:
    #         submenu_text = self.driver.find_element_by_id('submenu').get_attribute('textContent')
    #         # print(submenu_text)
    #         n = 0
    #         while (submenu_text == '' and n <20):
    #             #print('2')
    #             submenu_text = self.driver.find_element_by_id('submenu').get_attribute('textContent')
    #             n = n+1
    #     except Exception as msg:
    #         print('无法获取开始按钮的元素', msg)
    #
    #     self.find_element(self.menu_loc).click()
    #     time.sleep(2)
    #     self.find_element(self.role_loc).click()
    #     time.sleep(4)
    #
    # # 点击菜单--服务人员
    # def enter_agent(self):
    #     self.find_element(self.menu_loc).click()
    #     time.sleep(2)
    #     self.find_element(self.agent_loc).click()
    #     time.sleep(4)
    #


    # # 点击菜单--字段库
    # def enter_filed(self):
    #     self.find_element(self.menu_loc).click()
    #     time.sleep(2)
    #     self.find_element(self.field_loc).click()
    #     time.sleep(4)

    # 点击进入菜单--进入客户用户管理
    def enter_customer_user(self):
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.find_element(self.customer_user_loc).click()
        time.sleep(4)

    # 新建工单：进入工单模板使用页面--使用“TESTBED_测试流程”
    def enter_templateuse(self):
        # 点击“系统管理”
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        # 点击使用“TESTBED_测试流程”
        self.find_element(self.ticketcreate_loc).click()
        time.sleep(4)

    # 流程2：客户 A-1 使用的流程
    def enter_templateuse2(self):
        # 点击“系统管理”
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        # 点击使用“不同客户使用”
        self.find_element(self.ticketcreate2_loc).click()
        time.sleep(4)
    def enter_templateuse2_text(self):
        # 点击“系统管理”
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        # 打印“不同客户使用”
        return self.find_element(self.ticketcreate2_loc).text

