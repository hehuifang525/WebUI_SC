"""
@author: DT_testing
@file:   postmasterfilter_page.py
@desc:  【邮件过滤器】
@step：
"""
from selenium.webdriver.common.by import By
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PostmasterFilter_Page(Base):

    # 添加按钮
    addbtn_loc = (By.ID, 'fieldCreateButton')
    # 导入
    Import_loc = (By.CSS_SELECTOR, '[class="btn-group flex-start"] button:nth-child(3)')
    search_loc = (By.ID, 'Search-input')

    # 提交  CalendarSubmit
    submit_loc = (By.ID, 'CalendarSubmit')
    # 返回列表
    backlist_loc = (By.ID, 'CalendarCancel')



    # # 工单通知页面暂放
    # backlist01_loc = (By.ID, 'button.ant-btn:nth-child(2)')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')

    def clickadd(self):
        self.clickButton(self.addbtn_loc)

    # def backlist(self):
    #     '''工单通知，返回列表 '''
    #     self.clickButton(self.backlist01_loc)
    #     time.sleep(2)

    def clickImport(self):
        self.clickButton(self.Import_loc)
        time.sleep(2)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    def search(self, text):
        self.send_keys(self.search_loc, text)
        time.sleep(1)


    def backlist(self):
        self.find_element(self.backlist_loc).click()
        time.sleep(2)

