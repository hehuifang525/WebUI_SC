"""
@author: DT_testing
@file:   ticketgroup_page.py
@desc:  【工单分组】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class TicketGroupPage(Base):
    # 添加按钮
    addbtn_loc = (By.ID, 'AddTicket')
    import_loc = (By.ID, 'Import')
    search_loc = (By.ID, 'Search-input')
    tabvalid_loc = (By.ID, 'valid')
    tabinvalid_loc = (By.ID, 'invalid')
    table_head_loc = (By.CSS_SELECTOR, 'thead th')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    # 添加页面
    name_loc = (By.ID, 'Name')
    type_loc = (By.ID, 'Type')
    groupqueue_loc = (By.ID, 'GroupQueue')
    defaultrole_loc = (By.ID, 'DefaultRole')
    validID_loc = (By.ID, 'ValidID')
    comment_loc = (By.ID, 'Comment')
    # 选择要显示的字段
    choose_Field_loc = (By.ID, 'DynamicFieldSelect_Search')
    submit_loc = (By.ID, 'Submit')
    goBack_loc = (By.ID, 'GoBack')
    # 下一步
    nextstep_loc = (By.ID,'nextStep')

    def add(self):
        self.clickButton(self.addbtn_loc)

    def search(self, text):
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    def clickimport(self):
        self.clickButton(self.import_loc)

    def submit(self):
        self.clickButton(self.submit_loc)

    # 返回列表
    def backlist(self):
        self.clickButton(self.goBack_loc)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    # 点击下一步
    def nextstep(self):
        self.clickButton(self.nextstep_loc)

    def send_name(self, text):
        """
        名称输入值
        """
        self.send_keys(self.name_loc, text)





