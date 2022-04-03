"""
@author: DT_testing
@file:   notification_page.py
@desc:  【工单通知】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class NotificationPage(Base):
    addbth_loc = (By.ID, 'fieldCreateButton')
    Search_loc = (By.ID, 'Search-input')
    Search_result = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left')

    # 复制
    Copy_loc = (By.ID, 'Copy')

    #---添加页面
    Name_loc = (By.ID, 'Name')
    # 事件
    Events_loc =(By.ID, 'Events')
    # 第一个事件   ArticleAutoResponse
    ArticleAutoResponse_loc = (By.ID, 'ArticleAutoResponse')
    # 确定
    closeOption_loc = (By.ID,'closeOption')
    # 提交
    submit_loc = (By.CSS_SELECTOR, '.submit-btn button.ant-btn:nth-child(1)')
    # 返回列表
    backlist_loc = (By.CSS_SELECTOR, '.submit-btn button.ant-btn:nth-child(2)')
    # [class="btn-group flex-start"] button:nth-child(3)
    Import_loc = (By.CSS_SELECTOR, '[class="btn-group flex-start"] button:nth-child(3)')

    # 简体中文主题
    zh_CN_ubject_loc = (By.ID, 'zh_CN+Subject')
    # 内容
    body_loc =(By.CSS_SELECTOR, '[role="textbox"]')


    def add(self):
        self.clickButton(self.addbth_loc)

    def inputname(self, text):
        self.send_keys(self.Name_loc, text)

    def chose_first_eveents(self, text):
        '''选择事件'''
        self.find_element(self.Events_loc).click()

        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(0.5)
        # self.find_element(self.select_all_loc).click()
        # self.find_element(self.close_select_loc).click()
        title = 'nz-option-item[title="' + text + '"]'
        # print(title)
        elm_loc = (By.CSS_SELECTOR, title)
        self.find_element(elm_loc).click()

    def closeOption(self):
        self.clickButton(self.closeOption_loc)

    def submit(self):
        self.clickButton(self.submit_loc)

    def backlist(self):
        self.clickButton(self.backlist_loc)

    def Search(self,text):
        # 0118增加
        self.clickButton(self.Search_loc)
        self.send_keys(self.Search_loc, text)

    # 点击搜索结果
    def searckresult(self):
        self.find_elements(self.Search_result)[0].click()

    def Import(self):
        self.clickButton(self.Import_loc)

    def inputsubject(self, text):
        self.send_keys(self.zh_CN_ubject_loc, text)

    def inputbody(self, text):
        self.send_keys(self.body_loc, text)