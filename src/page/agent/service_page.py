"""
@author: DT_testing
@file:   service_page.py
@desc:  【服务】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base



class ServicePage(Base):
    addbtn_loc = (By.CSS_SELECTOR, '.flex-between-center.handle-group button:nth-child(1)')
    name_loc = (By.ID, 'Name')
    validinput_loc = (By.ID, 'ValidID')
    valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    invalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    Comment_loc = (By.ID, 'Comment')
    # 下一步，提交并返回列表  返回列表
    next_loc = (By.CSS_SELECTOR, '#step1 button:nth-child(1)')
    submitReturn_loc = (By.CSS_SELECTOR, '#step1 button:nth-child(2)')
    goBack1_loc = (By.CSS_SELECTOR, '#step1 button:nth-child(3)')
    right_search_loc = (By.ID, 'Search-input')

    # 服务关联项页面
    # 服务水平协议
    SLA_loc = (By.ID, 'SLA')
    select_all_loc = (By.ID, 'Select')
    close_select_loc = (By.ID, 'closeOption')
    # 删除服务协议
    delete_sla_loc = (By.CSS_SELECTOR, '#SLA .ant-select-close-icon')
    # 客户
    # 流程
    # 完成  、完成并再添加一条，上一步，返回列表
    complete_loc = (By.CSS_SELECTOR, '#step2 button:nth-child(1)')
    complete_add_loc = (By.CSS_SELECTOR, '#step2 button:nth-child(2)')
    previous_loc = (By.CSS_SELECTOR, '#step2 button:nth-child(3)')
    goBack2_loc = (By.CSS_SELECTOR, '#step2 button:nth-child(4)')


    # 导入导出按钮
    ImportExport_loc =(By.CSS_SELECTOR, '.flex-between-center.handle-group button:nth-child(2)')

    # 01 左侧导入按钮
    Import_left_loc = (By.CSS_SELECTOR, 'li#Import')
    # 02 左侧导出按钮
    Export_left_loc = (By.CSS_SELECTOR, 'li#Export')

    table_head_loc = (By.CSS_SELECTOR, '.theadtr.ant-table-row th')
    table_body_loc = (By.CSS_SELECTOR, '#baseTableTbody td.ant-table-cell-fix-left')
    # tableleftcell_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left-last')


    # 输入名称提示
    name_tip_loc = (By.ID, 'Name_errorServeMessage')

    # 导航路径 .ant-breadcrumb
    bar_loc = (By.CSS_SELECTOR, '.ant-breadcrumb')

    # 列表有效tab  valid
    validtab_loc = (By.ID, 'valid')
    # 列表无效tab




    def add(self):
        self.clickButton(self.addbtn_loc)
        time.sleep(3)

    # 导入导出页面---点击左侧导入按钮
    def click_Import_left(self):
        self.find_element(self.Import_left_loc).click()

    # 导入导出页面--点击左侧导出按钮
    def click_Export_left(self):
        self.clickButton(self.Export_left_loc)
        # self.find_element(self.Export_left_loc).click()

    def ImportExport(self):
        self.clickButton(self.ImportExport_loc)
        # self.find_element(self.ImportExport_loc).click()

    def inputname(self, text):
        self.send_keys(self.name_loc, text)
        time.sleep(2)

    def valid(self):
        self.find_element(self.validinput_loc).click()
        time.sleep(1)
        self.find_element(self.valid_loc).click()

    def invalid(self):
        self.find_element(self.validinput_loc).click()
        time.sleep(1)
        self.find_element(self.invalid_loc).click()

    # 提交并返回列表
    def submitreturn(self):
        self.find_element(self.submitReturn_loc).click()
        time.sleep(1)

    # 点击下一步
    def next(self):
        self.clickButton(self.next_loc)
        # self.find_element(self.next_loc).click()
        # self.find_element(self.complete_loc)

    # 点击上一步 previous_loc
    def previous(self):
        self.find_element(self.previous_loc).click()

    # 第二步中点击完成  complete
    def complete(self):
        self.clickButton(self.complete_loc)
        # self.find_element(self.complete_loc).click()
        # 点击完成后，返回等待添加按钮出现后再继续操作
        self.find_element(self.addbtn_loc)

    # 完成并添加下一条  complete_add_loc
    def complete_add(self):
        self.find_element(self.complete_add_loc).click()

    # 右侧搜索
    def right_search(self, text):
        # self.find_element(self.right_search_loc).clear()
        self.send_keys(self.right_search_loc, text)
        time.sleep(1)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    # 基本信息-返回列表
    def goBack1(self):
        self.find_element(self.goBack1_loc).click()
        self.find_element(self.addbtn_loc)
        time.sleep(1)

    # 服务关联项-返回列表
    def goBack2(self):
        self.find_element(self.goBack2_loc).click()
        time.sleep(1)

    # 取 名称值
    def getname(self):
        return self.find_element(self.name_loc).get_attribute('value')

    # 判断提交并返回按钮，下一步按钮是否可点击
    def is_disabled(self, text):
        isdisabled = ''
        if text == '下一步':
            isdisabled = self.find_element(self.next_loc).get_attribute('disabled')
        elif text == '提交并返回列表':
            isdisabled= self.find_element(self.submitReturn_loc).get_attribute('disabled')
        return isdisabled

    def gettable_head(self):
        # 取表头字段
        return self.find_elements(self.table_head_loc)

    # 取名称校验提示
    def getnametip(self):
        return self.find_element(self.name_tip_loc).text

    # 服务关联项关联搜索并选择服务协议
    def choose_sla(self, text):
        self.find_element(self.SLA_loc).click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(0.5)
        self.find_element(self.select_all_loc).click()
        self.find_element(self.close_select_loc).click()

    # 取关联协议的显示值
    def Association_sla(self):
        return self.find_element(self.SLA_loc).text

    def delete_all_sla(self):
        move_btn = self.driver.find_element_by_id('SLA')
        ActionChains(self.driver).move_to_element(move_btn).perform()
        # time.sleep(0.5)
        self.find_element(self.delete_sla_loc).click()

    # 获取导航路径，有主页小房子的部分
    def getbar(self):
        return self.find_element(self.bar_loc).text

        # 取服务协议最左侧的名称列

    def getleftslaname(self):
        return self.find_elements(self.table_body_loc)

    def get_tab_text(self):
        return self.find_element(self.validtab_loc).text




