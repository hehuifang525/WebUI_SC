"""
@author: DT_testing
@file:   district_page.py
@desc:  【区域】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class DistrictPage(Base):
    # 四个按钮（添加、导入导出、导出当前、打印）
    add_loc = (By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary:nth-child(1)')
    # 导入导出
    ImportExport_loc = (By.CSS_SELECTOR, '[class="flex-start margin-T15"] button:nth-child(2)')
    # 有效无效tab
    validtab_loc = (By.CSS_SELECTOR, '[role = "tab"]')
    # 左侧搜索区域
    left_Search_loc = (By.CSS_SELECTOR, 'class="ant-input ng-valid ng-star-inserted ng-dirty ng-touched"')
    # 右侧搜索
    right_Search_loc = (By.ID, 'Search-input')
    # 表头
    table_head_loc = (By.CSS_SELECTOR, '.ant-table-fixed thead th')
    # 表格数据
    table_body_loc = (By.CSS_SELECTOR, 'td.ant-table-cell.ng-star-inserted')
    # 表格最左边列
    tableleftcell_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left-last')
    # 路径、tab标题
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    tabtitle_loc = (By.CSS_SELECTOR, '.nav-horizontal-active [class="nav-horizontal-title ellipsis-row"]')
    # empty_loc = (By.CSS_SELECTOR, '[class="ant-empty-normal ant-empty ng-star-inserted"] p')
    empty_loc = (By.CSS_SELECTOR, 'p.ant-empty-description')
    # 导入页面左侧导出
    left_Export_loc =(By.CSS_SELECTOR, 'li#Export')


    # 添加页面
    name_loc = (By.ID, 'Name')
    name_tip_loc =(By.ID, 'Name_errorServeMessage')
    Parent_district_loc = (By.ID, 'ParentID')
    valid_input_loc = (By.ID, 'ValidID')
    # valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    # invalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    # 0817 修改
    valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(2)')
    invalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(1)')
    Comment_loc = (By.ID, 'Comment')
    # 添加页面两按钮（提交、返回列表）
    submit_loc = (By.CSS_SELECTOR, '.firstStep-btn button.ant-btn:nth-child(1)')
    backlist_loc = (By.CSS_SELECTOR, '.firstStep-btn button.ant-btn:nth-child(2)')

    valid_clear_loc = (By.CSS_SELECTOR, '#ValidID .ant-select-clear.ng-star-inserted')

    def gettable_head(self):
        return self.find_elements(self.table_head_loc)

    def gettable_body(self):
        return self.find_elements(self.table_body_loc)

    def getleftslaname(self):
        return self.find_elements(self.tableleftcell_loc)

    # 取页面gettabTitle
    def gettabTitle(self):
        return self.find_element(self.tabtitle_loc).text

    def get_empty_tip(self):
        return self.find_element(self.empty_loc).text

    # 取road路径标题
    def getroadText(self):
        return self.find_element(self.road_loc).text

    def click_add(self):
        self.clickButton(self.add_loc)
        time.sleep(2)

    def check_add_clickable(self):
        return self.find_element(self.add_loc).is_enabled()

    # 点击有效tab 无效tab
    def click_valid_tab(self):
        self.find_elements(self.validtab_loc)[0].click()

    def click_invalid_tab(self):
        self.find_elements(self.validtab_loc)[1].click()
        time.sleep(2)


    # 添加页面
    def input_name(self, text):
        self.send_keys(self.name_loc, text)

    def get_name(self):
        return self.find_element(self.name_loc).get_attribute('testvalue')

    def get_name_tip(self):
        return self.find_element(self.name_tip_loc).text

    def choose_parent_district(self, text):
        title = '[title="' + text + '"]'
        self.driver.find_element(*self.Parent_district_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        elment = self.driver.find_elements_by_css_selector(title)
        elme = elment[1]
        elme.click()


        # self.driver.find_element(*self.tarname2_loc).click()
        # time.sleep(2)
        # ActionChains(self.driver).send_keys(text).perform()
        # self.driver.find_element_by_css_selector('[title="' + text + '"]').click()


    def get_parent_district(self):
        # return self.find_element(self.Parent_district_loc).get_attribute('value')
        return self.driver.find_element_by_css_selector('#ParentID input').get_attribute('value')

    def choose_valid(self):
        self.clickButton(self.valid_input_loc)
        time.sleep(1)
        self.clickButton(self.valid_loc)

    def choose_invalid(self):
        self.clickButton(self.valid_input_loc)
        # time.sleep(1)
        self.clickButton(self.invalid_loc)

    def get_valid(self):
        return self.find_element(self.valid_input_loc).text


    def addsubmit(self):
        self.clickButton(self.submit_loc)
        # self.find_element(self.submit_loc).click()
        time.sleep(3)

    # 判断提交按钮是否可以点击
    def check_submit_clickable(self):
        return self.find_element(self.submit_loc).is_enabled()

    # 删除有效性
    def delete_valid(self):
        elenmt = self.find_element(self.valid_input_loc)
        ActionChains(self.driver).move_to_element(elenmt).perform()
        time.sleep(1)
        self.clickButton(self.valid_clear_loc)

    def input_coment(self, text):
        self.send_keys(self.Comment_loc, text)

    def get_coment(self):
        return self.find_element(self.Comment_loc).get_attribute('testvalue')

    def backlist(self):
        self.find_element(self.backlist_loc).click()
        time.sleep(2)

    # 右侧搜索区域
    def search(self, text):
        self.find_element(self.right_Search_loc).click()
        self.send_keys(self.right_Search_loc, text)
        time.sleep(2)

    def click_search_result(self):

        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(2)

    def import_export(self):
        self.clickButton(self.ImportExport_loc)

    def left_export(self):
        self.clickButton(self.left_Export_loc)

