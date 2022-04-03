"""
@author: DT
@file:   table_page.py
@desc:  【系统表格列表统一定位】
@step： 目前使用模板有（1）工单模板-表头，（2）checkelement中字段影响关系，(3)内容模板 其他模板调整接入
"""
from selenium.webdriver.common.by import By

from common.base import Base
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TablePage(Base):
    # 列表表头字段
    tableth_loc = (By.CSS_SELECTOR, 'th.ant-table-cell')

    # 表格样式1：无删除多选框，如服务模块、字段影响关系、角色等
    table_body_style01_loc = (By.CSS_SELECTOR, '#baseTableTbody td.ant-table-cell-fix-left')


    # # 表格样式2：表第一行为多选框，如字段库，工单模板
    # searchresult_loc = (By.CSS_SELECTOR, '.cursor.ant-table-row.ng-star-inserted')

    # 取列表表头字段，样式1，样式2通用
    def gettableth(self):
        return self.find_elements(self.tableth_loc)

    # 样式1：点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_style01_loc)[0].click()
        time.sleep(1)

    # # 样式2：点击搜索结果
    # def search_result02(self):
    #     self.clickButton(self.searchresult_loc)
    #     time.sleep(1)
