"""
@author: DT_testing
@file:   fieldimpacts_page.py
@desc:  【字段影响关系】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class FieldimpactsPage(Base):
    # 添加按钮
    addbtn_loc = (By.ID, 'fieldCreateButton')
    search_loc = (By.CSS_SELECTOR, '#Search-input input')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')

    # 添加页面
    name_loc = (By.ID, 'Name')
    object_loc = (By.ID, 'Object')
    # 对象--资产
    object_cmdb_loc = (By.ID, 'CMDB')
    # 对象-工单
    object_ticket_loc = (By.ID, 'Ticket')
    comment_loc =(By.ID,'Comment')
    Validinput_loc = (By.ID,'ValidID')
    #
    Valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    inValid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    # 选择字段
    field_search_loc = (By.ID, 'Field_Search')
    # 选择下拉的第一个字段
    choose_field_loc = (By.CSS_SELECTOR, '[class="ant-select-item-option-content"]')
    # .tree-box-right button
    addfieldbtn_loc =(By.CSS_SELECTOR, '.tree-box-right button')

    # 字段---工单流转状态  TicketFlowStats
    TicketFlowStats_loc =(By.ID, 'TicketFlowStats')
    # 选择全部
    selectall_loc = (By.ID, 'Select')
    # 确定--关闭下拉选择框
    closeOption_loc = (By.ID, 'closeOption')
    # 保存并返回列表
    sumbit_return_loc = (By.CSS_SELECTOR, '.flex-justify-center button.ant-btn:nth-child(1)')
    # 删除
    # detele_loc = (By.ID, 'Delete')
    detele_loc = (By.CSS_SELECTOR, 'tr[style=""] #Delete')
    # .ant-modal-confirm-btns button:nth-child(2)
    detele_comfirm_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-btns button:nth-child(2)')
    # 返回列表
    backlist_loc = (By.CSS_SELECTOR, '.flex-justify-center button.ant-btn:nth-child(2)')


    def add(self):
        self.clickButton(self.addbtn_loc)

    def search(self, text):
        self.find_element(self.search_loc).click()
        # self.clickButton(self.search_loc)
        self.find_element(self.search_loc).clear()
        # self.send_keys(self.search_loc, text)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(1)

    # 返回列表
    def backlist(self):
        self.clickButton(self.backlist_loc)
        time.sleep(1)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    def inputname(self, text):
        self.send_keys(self.name_loc, text)

    # 点击对象
    def obejctclick(self):
        self.clickButton(self.object_loc)

    # 对象选择工单
    def  choose_tikect(self, text):
        title = 'nz-option-item[title="' + text + '"]'
        # print(title)
        elm_loc = (By.CSS_SELECTOR, title)
        self.find_element(elm_loc).click()
        # self.clickButton(self.object_ticket_loc)

    # 点击选择字段
    def choosefiled(self):
        self.clickButton(self.choose_field_loc)

    # 选择第一个字段
    def choose_field(self):
        self.clickButton(self.choose_field_loc)
        time.sleep(1)

    # 点击添加按钮
    def addfield(self):
        self.clickButton(self.addfieldbtn_loc)
        time.sleep(1)

    def sumbit_return(self):
        self.clickButton(self.sumbit_return_loc)
        time.sleep(3)

    # 搜索字段
    def field_search(self, text):
        self.find_element(self.field_search_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        # self.send_keys(self.field_search_loc, text)

    def choose_FlowStats_all(self):
        time.sleep(1)
        self.clickButton(self.TicketFlowStats_loc)
        self.clickButton(self.selectall_loc)
        self.clickButton(self.closeOption_loc)

    def detele(self):
        '''
            删除按钮定位到2个，点击第二个删除
        '''
        # self.find_elements(self.detele_loc)[1].click()
        self.find_element(self.detele_loc).click()
        # self.clickButton(self.detele_loc)

    def detele_comfirm(self):
        self.clickButton(self.detele_comfirm_loc)












