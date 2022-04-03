"""
@author: DT_testing
@file:   slacalender_page.py
@desc:  【工作时间管理】
@step：
"""
from selenium.webdriver.common.by import By
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SlacalenderPage(Base):

    # 添加按钮
    addbtn_loc = (By.CSS_SELECTOR, '[id="fieldCreateButton width90"]')
    search_loc = (By.ID, 'Search-input')
    table_head_loc = (By.CSS_SELECTOR, '.ant-table-thead th')
    # table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    # 0922 修改
    table_body_loc = (By.CSS_SELECTOR, 'table .ant-table-tbody>tr td')

    # #tableTbody .ant-table-cell.ng-star-inserted
    table_body_list_loc = (By.CSS_SELECTOR, '#tableTbody .ant-table-cell.ng-star-inserted')

    # 全部（数量）tab   # 32版本取消显示
    all_tab_loc = (By.CSS_SELECTOR, '[role="tab"]')

    # .ant-empty p
    empty_loc = (By.CSS_SELECTOR, '.ant-empty p')

    # 添加页面
    name_loc = (By.ID, 'Name')
    # 时区
    time_zone_loc = (By.ID, 'TimeZone')
    # 周起始日
    week_day_start_loc = (By.ID, 'WeekDayStart')
    # 有效性
    validinput_loc = (By.ID, 'ValidID')
    # 0817修改
    # valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    # invalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(2)')
    invalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(1)')
    # 备注
    comment_loc = (By.ID, 'Comment')
    # 提交  CalendarSubmit
    submit_loc = (By.ID, 'CalendarSubmit')
    # 返回列表
    goback1_loc = (By.ID, 'CalendarCancel')
    # 输入名称提示
    name_tip_loc = (By.ID, 'Name_errorServeMessage')
    chose_date_loc = (By.CSS_SELECTOR, '[placeholder="选择日期"]')
    now_loc = (By.CSS_SELECTOR, '[class="ant-picker-now-btn"]')
    confirm_loc = (By.CSS_SELECTOR, '.ant-btn-sm')
    # 休假日、指定工作日后面的输入名称按钮
    input_name_loc = (By.CSS_SELECTOR,'[class="datePickerinput"]')
    add_icon_loc = (By.CSS_SELECTOR,'.ant-btn-dashed')
    # 删除休假日、指定工作日（删除图标）
    del_icon_loc =(By.CSS_SELECTOR, '.ant-btn-icon-only')

    # 清除所有的工作时间选择（表格中）

    clear_time_loc = (By.CSS_SELECTOR, '[title="取消所有选中"]')
    # [class="ng-star-inserted cur"]
    # 被选中的工作时间
    selected_time_loc = (By.CSS_SELECTOR, '.cur.ng-star-inserted')


    # # 取名称校验提示
    # def getnametip(self):
    #     return self.find_element(self.name_tip_loc).text

    def table_head(self):
        # 取表头字段
        return self.find_elements(self.table_head_loc)

    def clickadd(self):
        self.clickButton(self.addbtn_loc)
        time.sleep(2)

    # 右侧搜索
    def search(self, text):
        # self.find_element(self.right_search_loc).clear()
        # Base(self.driver).move_to_pagetop()
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    # 添加页面
    # 输入名称
    def inputname(self, text):
        self.send_keys(self.name_loc, text)
        time.sleep(1)

    # 取名称值
    def getname(self):
        return self.find_element(self.name_loc).get_attribute('value')

    # 取名称校验提示
    def getnametip(self):
        return self.find_element(self.name_tip_loc).text

    def valid(self):
        self.find_element(self.validinput_loc).click()
        time.sleep(1)
        self.find_element(self.valid_loc).click()

    def invalid(self):
        Base(self.driver).move_to_pagebottom()
        self.find_element(self.validinput_loc).click()
        time.sleep(1)
        self.find_element(self.invalid_loc).click()

    def goback(self):
        self.find_element(self.goback1_loc).click()
        time.sleep(6)

    # 提交
    def submit(self):
        self.find_element(self.submit_loc).click()
        time.sleep(1)

    def getleftslaname(self):
        return self.find_elements(self.table_body_loc)

    def gettabblelist(self):
        return self.find_elements(self.table_body_list_loc)

    def get_tab_text(self):
        return self.find_element(self.all_tab_loc).text

    def get_empty_text(self):
        '''取列表中，无记录时的文字描述'''
        return self.find_element(self.empty_loc).text

    # 检查提交按钮
    def is_disabled(self):
        return self.find_element(self.submit_loc).get_attribute('disabled')

    # 输入此刻的日期
    def chose_date(self, num):
        self.driver.find_elements_by_css_selector("[placeholder='选择日期']")[num].click()
        time.sleep(0.5)
        self.find_element(self.now_loc).click()
        self.find_element(self.confirm_loc).click()

    # 输入指定日期
    def chose_date2(self, num, text):
        self.driver.find_elements(By.CSS_SELECTOR,"[placeholder='选择日期']")[num].clear()
        # self.driver.find_elements_by_css_selector("[placeholder='选择日期']")[num].clear()
        self.driver.find_elements(By.CSS_SELECTOR,"[placeholder='选择日期']")[num].click()
        # self.driver.find_elements_by_css_selector("[placeholder='选择日期']")[num].click()
        time.sleep(0.5)
        self.driver.find_elements(By.CSS_SELECTOR, "[placeholder='选择日期']")[num].send_keys(text)
        self.find_element(self.confirm_loc).click()

    def input_name2(self, num, text):
        '''
        :param num: 在第几个名称中输入
        :param text: 具体输入的内容
        :return:  输入休假日、指定找工作日后面的名称
        '''
        self.driver.find_elements_by_css_selector("[placeholder='输入名称']")[num].clear()
        self.driver.find_elements_by_css_selector("[placeholder='输入名称']")[num].send_keys(text)

    def comment(self, text):
        self.send_keys(self.comment_loc, text)

    def clear_comment(self):
        self.find_element(self.comment_loc).clear()

    def get_comment(self):
        return self.find_element(self.comment_loc).get_attribute('value')

    # 添加休假日、指定工作日
    def add_data(self, num = 0):
        '''
        :param num: 0 为添加休假日、 1为添加指定工作日
        :return:
        '''
        self.find_elements(self.add_icon_loc)[num].click()

    # 取休假日、指定工作日的日期，以及名称
    def get_data(self, num):
        return self.driver.find_elements_by_css_selector("[placeholder='选择日期']")[num].get_attribute("value")

    def get_data_name(self, num):
        return self.driver.find_elements_by_css_selector("[placeholder='输入名称']")[num].get_attribute("value")

    def del_date(self, num):
        self.find_elements(self.del_icon_loc)[num].click()

    # 返回元素的个数
    def get_data_num(self):
        elements = self.driver.find_elements_by_css_selector("[placeholder='选择日期']")
        return len(elements)

    # 工作时间表格相关操作
    def clear_time(self):
        self.find_element(self.clear_time_loc).click()

    def chose_time(self, num):
        # title = '#j_ul span[title=' + text + '"]'
        title = '[class="overflow-auto"] span'
        self.driver.find_elements_by_css_selector(title)[num].click()

    def get_selected_time_num(self):
        return len(self.find_elements(self.selected_time_loc))





