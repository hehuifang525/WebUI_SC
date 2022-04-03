"""
@author: DT_testing
@file:   agent_home_page.py
@desc:  【服务人员主页】
@step：
"""

from selenium.webdriver.common.by import By
from common.base import Base
import time
from selenium.webdriver import ActionChains


class AgentHomePage(Base):
    # 未关闭工单
    open_ticket_loc = (By.CSS_SELECTOR,'[title="工单所有者是我，并且没有关闭的工单"]')
    # 我参与的工单 participate
    participate_ticket_loc = (By.CSS_SELECTOR,'[title="我参与并且未关闭的工单"]')
    # 升级工单
    upgrade_ticket_loc = (By.CSS_SELECTOR,'[title="工单指定处理人是我，并且升级的工单"]')
    # 主页图标
    home_ico_loc = (By.CSS_SELECTOR,'.anticon-home')
    # 设置按钮
    set_ico_loc = (By.CSS_SELECTOR,'div.config-fixed')
    # 保存设置
    sumbit_set_loc = (By.CSS_SELECTOR, '.ant-drawer-open .ant-checkbox-group button')

    # 当前tab .cursor.nav-horizontal-active .flex-space-between
    active_tab_loc = (By.CSS_SELECTOR,'.cursor.nav-horizontal-active .flex-space-between')

    def home(self):
        self.clickButton(self.home_ico_loc)
        # self.find_element(self.home_ico_loc).click()

    def open_ticket(self):
        self.clickButton(self.open_ticket_loc)
        # self.find_element(self.open_ticket_loc).click()

    def participate_ticket(self):
        self.clickButton(self.participate_ticket_loc)
        # self.find_element(self.participate_ticket_loc).click()

    def upgrade_ticket(self):
        self.clickButton(self.upgrade_ticket_loc)
        # self.find_element(self.upgrade_ticket_loc).click()

    def set_ico(self):
        self.clickButton(self.set_ico_loc)
        # self.find_element(self.set_ico_loc).click()

    def sumbit_set(self):
        self.clickButton(self.sumbit_set_loc)
        # self.find_element(self.sumbit_set_loc).click()

    def active_tab(self):
        return self.find_element(self.active_tab_loc).text
