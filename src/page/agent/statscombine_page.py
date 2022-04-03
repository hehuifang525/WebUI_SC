"""
@author: DT_testing
@file:   statscombine_page.py
@desc:  【统计管理组合管理】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base
from selenium.webdriver.common.keys import Keys


class StatscombinePage(Base):
    addbtn_loc = (By.XPATH, '//*[@id="newHeight"]/div/nz-spin/div/div/app-stats-combine/nz-spin/div/div/div[1]/button')
    search_loc = (By.ID, 'Search-input')
    name_loc =(By.ID, 'Name')
    table_head_loc = (By.CSS_SELECTOR, 'thead th')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    baseSubmit_loc = (By.ID, 'baseSubmit')
    baseCancel_loc = (By.ID, 'baseCancel')

    def addstatscombine(self):
        self.clickButton(self.addbtn_loc)

    # 右侧搜索
    def search(self, text):
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    # 输入名称
    def inputname(self,text):
        self.send_keys(self.name_loc, text)

    def submit(self):
        self.find_element(self.baseSubmit_loc).click()
        time.sleep(2)

    # 返回列表
    def backlist(self):
        self.find_element(self.baseCancel_loc).click()

