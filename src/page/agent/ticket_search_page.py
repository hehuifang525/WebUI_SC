"""
@author: DT_testing
@file:   ticket_search_page.py
@desc:  【工单搜索】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class TicketSearchPage(Base):
    Fulltext_loc = (By.CSS_SELECTOR, '.dynamic-fields .ant-spin-container .ant-form-item-control-input input')
    searchbtn_loc = (By.CSS_SELECTOR, '.ticket-search-resultFormat.ant-row  button')
    # 添加模板按钮
    addtemp_loc = (By.CSS_SELECTOR, '[data-icon="plus-circle"]')
    # 模板名称
    tempname_loc = (By.CSS_SELECTOR, '.template-name .ant-form-item-control-input-content input')
    # 保存模板
    savetemp_loc = (By.CSS_SELECTOR, '.template-name button:nth-child(1)')
    # 取消模板编辑
    closetemp_loc = (By.CSS_SELECTOR, '.template-name button:nth-child(2)')
    # 搜索模板 searchtickettemplate
    search_temp_loc =(By.ID, 'searchtickettemplate')
    # .cdk-virtual-scroll-content-wrapper .ant-select-item-option-content
    temp_item_loc = (By.CSS_SELECTOR,'.cdk-virtual-scroll-content-wrapper .ant-select-item-option-content')

    # 导航栏，工单-知识库搜搜输入框
    bar_search_loc =(By.ID, 'FreeSearch')
    # 导航栏，点击搜索工单
    bar_search_ticket_loc = (By.CSS_SELECTOR, '#searchList0 #ticket')
    # 导航栏，单击搜索知识库
    bar_search_faq_loc = (By.CSS_SELECTOR, '#searchList1 #FAQ')
    # 导航栏，工单搜索模板
    bar_template_loc = (By.CSS_SELECTOR, 'a.header-template-search-title')

    # 点击搜索按钮
    def search(self):
        self.find_element(self.searchbtn_loc).click()

    # 全文输入搜索内容
    def fulltext(self, text):
        self.send_keys(self.Fulltext_loc, text)

    # 点击添加模板
    def addtemp(self):
        self.find_element(self.addtemp_loc).click()

    # 创建模板输入名称
    def tempname(self, text):
        self.send_keys(self.tempname_loc, text)

    # 保存模板
    def savetemp(self):
        self.find_element(self.savetemp_loc).click()

    # 导航栏输入搜索内容
    def bar_search_input(self, text):
        self.send_keys(self.bar_search_loc, text)

    # 搜索模板
    def search_temp(self, temp):
        self.find_element(self.search_temp_loc).click()
        time.sleep(0.5)
        ActionChains(self.driver).send_keys(temp).perform()
        self.find_element(self.temp_item_loc).click()

    # 搜工单
    def search_ticket(self):
        self.find_element(self.bar_search_ticket_loc).click()

    # 搜知识库
    def search_faq(self):
        self.find_element(self.bar_search_faq_loc).click()

    # bar 导航中选择一个搜索模板
    def bar_temp_search(self, temp):
        self.find_element(self.bar_template_loc).click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector('[title="' + temp + '"]').click()
        time.sleep(2)
