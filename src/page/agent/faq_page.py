"""
@author: DT_testing
@file:   faq_page.py
@desc:  【知识库类别管理】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base
from selenium.webdriver.common.keys import Keys


class FaqPage(Base):
    # 左上角路径
    bar_loc =(By.CSS_SELECTOR, 'div.breadcrumb-overflow')
    tab_title_loc = (By.CSS_SELECTOR,'ul .nav-horizontal-active')
    addbtn_loc = (By.ID, 'addCatalog')
    name_loc = (By.ID, 'Name')
    validinput_loc = (By.ID, 'ValidID')
	# 0817修改
    valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(2)')
    invalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(1)')
    # valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    # invalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    # 父类别
    parent_loc = (By.ID,'ParentID')
    # 选择命中的高亮
    highlight_loc = (By.CSS_SELECTOR, '.font-highlight')

    Comment_loc = (By.ID, 'Comment')
    # 下一步，提交并返回列表  返回列表
    next_loc = (By.ID, 'next')
    submitReturn_loc = (By.ID, 'submitReturn')
    goBack1_loc = (By.ID, 'goBack1')
    right_search_loc =(By.ID, 'searchInput')
    delete_loc = (By.ID, 'Delete')
    # 取消删除、确认删除
    cancle_detele_loc =(By.CSS_SELECTOR,'.ant-modal-confirm-body-wrapper button:nth-child(1)')
    # [role="document"]  button:nth-child(2)
    comfire_detele_loc = (By.CSS_SELECTOR, '[role="document"] button:nth-child(2)')
    empty_loc = (By.CSS_SELECTOR, '[class="empty-text ng-star-inserted"] span')

    # 删除提示语
    detele_tip_loc = (By.CSS_SELECTOR, '.ant-modal-body p')
    # 无法删除弹框的确定按钮  #ok
    ok_loc = (By.ID, 'ok')



    # 表格最左边列
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    # 表格 各个单元格
    table_list_td_loc = (By.CSS_SELECTOR, '#tableTbody .cdk-drag td')

    # 类别关联项的完成、完成并再添加一条 上一步  返回列表按钮
    finished_loc = (By.ID, 'finished')
    finishAnother_loc = (By.ID, 'finishAnother')
    previous_loc = (By.ID, 'previous')
    goBack2_loc = (By.ID, 'goBack2')

    # 左侧搜索
    left_Search_loc = (By.ID, 'Search-tree')
    # 左侧搜索的父级显示
    parent_tree_loc = (By.CSS_SELECTOR, '.ant-tree-treenode-switcher-open')

    # 角色只读
    # RoleRo
    roleRo_loc = (By.ID, 'RoleRo')
    roleRW_loc = (By.ID, 'RoleRW')
    LinkCompany_loc = (By.ID, 'LinkCompany')

    # 取左上角路径值
    def get_bar(self):
        return self.find_element(self.bar_loc).text

    def tab_title(self):
        return self.find_element(self.tab_title_loc).text


    def add(self):
        self.find_element(self.addbtn_loc).click()

    def inputname(self, text):
        self.send_keys(self.name_loc, text)

    def inputcommen(self, text):
        self.send_keys(self.Comment_loc, text)

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

    def next(self):
        self.find_element(self.next_loc).click()

    def goback1(self):
        self.find_element(self.goBack1_loc).click()

    def finished(self):
        self.find_element(self.finished_loc).click()

    def finish_another(self):
        self.find_element(self.finishAnother_loc).click()

    def previous(self):
        self.find_element(self.previous_loc).click()

    def goback2(self):
        self.find_element(self.goBack2_loc).click()

    # 右侧搜索
    def right_search(self,text):
        self.find_element(self.right_search_loc).click()
        # self.clickButton(self.right_search_loc)
        # self.find_element(self.right_search_loc).clear()
        self.send_keys(self.right_search_loc, text)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()

    # 删除类别
    def detele(self):
        self.clickButton(self.delete_loc)
        time.sleep(1)
        # self.find_element(self.delete_loc).click()

    def cancle_delete(self):
        self.find_element(self.cancle_detele_loc).click()

    # 多次遇到确定删除按钮触发不了
    def comfire_delete(self):
        # self.clickButton(self.comfire_detele_loc)
        self.find_element(self.comfire_detele_loc).click()

    def get_detele_tip(self):
        return self.find_element(self.detele_tip_loc).text

    def clickok(self):
        self.find_element(self.ok_loc).click()
        time.sleep(2)

    # 取空的列表描述
    def getempty(self):
        # return self.find_element(self.empty_loc).get_attribute('innerText')
        return self.find_element(self.empty_loc).text

    # 取名称字段值
    def get_name(self):
        return self.find_element(self.name_loc).get_attribute("value")

    # 返回列表各个单元格值  table_list_td
    def table_list_td(self):
        return self.find_elements(self.table_list_td_loc)

    # 选择父级
    def parent(self, text):
        self.driver.find_element(*self.parent_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        # self.find_elements(self.highlight_loc)[0].click()
        self.driver.find_element_by_css_selector('.ant-select-tree-list-holder-inner [title="' + text + '"]').click()

    # 左侧搜索数据
    def left_search(self, text):
        self.send_keys(self.left_Search_loc, text)

    def get_parent_tree(self):
        return self.find_element(self.parent_tree_loc).text

    # 选择角色
    def rolero(self, text):
        self.driver.find_element(*self.roleRo_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        # self.find_elements(self.highlight_loc)[0].click()
        # title="系统默认角色"  按title点击
        # 退出
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()

        ActionChains(self.driver).move_to_element(self.find_element(
            self.roleRo_loc)).send_keys(Keys.ESCAPE).perform()

    # 选择角色
    def rolerw(self, text):
        self.driver.find_element(*self.roleRW_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.driver.find_element_by_css_selector('.ant-select-tree-list-holder-inner [title="' + text + '"]').click()
        # self.find_elements(self.highlight_loc)[0].click()
        # 退出
        ActionChains(self.driver).move_to_element(self.find_element(
            self.roleRW_loc)).send_keys(Keys.ESCAPE).perform()

    # 选择客户
    def LinkCompany(self, text):
        self.driver.find_element(*self.LinkCompany_loc).click()
        time.sleep(7)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        # self.find_elements(self.highlight_loc)[0].click()
        # 退出
        ActionChains(self.driver).move_to_element(self.find_element(
            self.LinkCompany_loc)).send_keys(Keys.ESCAPE).perform()

    # 取角色、客户输入值
    def get_rolero(self):
        return self.find_element(self.roleRo_loc).text

    def get_rolerw(self):
        return self.find_element(self.roleRW_loc).text

    def get_Company(self):
        return self.find_element(self.LinkCompany_loc).text