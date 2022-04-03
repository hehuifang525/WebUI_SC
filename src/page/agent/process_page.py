"""
@author: DT_testing
@file:   process_page.py
@desc:  【流程管理】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class ProcessPage(Base):
    # 添加按钮
    addbtn_loc = (By.CSS_SELECTOR, '[class="process-list-addBtn ant-btn"]:nth-child(1)')
    import_loc = (By.CSS_SELECTOR, '[class="process-list-addBtn ant-btn"]:nth-child(3)')
    search_loc = (By.ID, 'Search-input')

    table_head_loc = (By.CSS_SELECTOR, 'thead th')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    # 左侧业务类型搜索
    process_type_search_loc = (By.ID, 'process-type-search')

    # 保存并返回列表
    SaveReturn_loc = (By.ID, 'SaveReturn')
    # 保存
    Save_loc = (By.ID, 'process-submit')
    # 导入页面的返回列表
    goBack_loc = (By.ID, 'GoBack')
    # tab 关闭
    closetab_loc = (By.CSS_SELECTOR, '.nav-horizontal-active .delete')

    # 添加流程业务类型 process-type-add
    process_type_add_loc = (By.ID, 'process-type-add')
    type_name_loc = (By.ID, 'name')
    type_sumbit_loc =(By.CSS_SELECTOR, '.ant-modal-footer button')
    type_valid_input_loc = (By.ID,'valid')
    type_valid_loc = (By.CSS_SELECTOR, '[title="有效"]')
    type_invalid_loc = (By.CSS_SELECTOR, '[title="无效"]')

    # 关闭添加业务类型窗口
    close_type_loc = (By.CSS_SELECTOR, '.ant-modal-close-x')
    type_name_errorServeMessage_loc = (By.ID, 'name_errorServeMessage')
    # 名称
    name_errorServeMessage_loc = (By.CSS_SELECTOR, '.ant-form-item-explain')

    # 右侧流程为空的描述
    process_empty_loc = (By.CSS_SELECTOR, '.empty-text')
    # 搜索结果
    process_type_search_result_loc = (By.ID, '.ant-tree-treenode-selected')

    # 流程名称
    process_name_loc = (By.CSS_SELECTOR, '.ant-input-sm')
    # 描述
    describe_loc = (By.CSS_SELECTOR, '.ant-form-item-control-input-content textarea.ant-input')

    # 列表
    table_body_list_loc = (By.CSS_SELECTOR, '#tableTbody .ant-table-cell.ng-star-inserted')

    # 流程节点添加按钮
    add_link_opration_button_loc = (By.ID, 'link-opration-button')

    # 画布
    canvas_loc = (By.ID, 'flow_chart')

    # 后退 process-back-operate
    process_back_operate_loc = (By.ID, 'process-back-operate')

    #  [class="link-opration-template zIndex jtk-managed jtk-draggable jtk-droppable jtk-connected"] :nth-child(2)
    first_node_loc = (By.CSS_SELECTOR, '.jtk-managed')

    # 线条  [class="jtk-connector cursor"]
    line_loc = (By.CSS_SELECTOR, '[class="jtk-connector cursor"]')

    delete_line_loc = (By.CSS_SELECTOR, '[id="process-delete"]')

    cancle_detele_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-body-wrapper button:nth-child(1)')
    # [role="document"]  button:nth-child(2)
    comfire_detele_loc = (By.CSS_SELECTOR, '[role="document"] button:nth-child(2)')

    # 状态 描述等可以用这个
    input_loc = (By.CSS_SELECTOR, '.ant-form-item-control-input')
    # 选择状态  div.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(3)
    process_status_loc = (By.CSS_SELECTOR,'div.cdk-virtual-scroll-content-wrapper nz-option-item')
    process_tr_loc = (By.CSS_SELECTOR, '[id="tableTbody"] tr.cdk-drag')

    # 取流程表中的颜色
    def get_tr_color(self):
        self.find_elements(self.process_tr_loc)[0].get_attribute('outerHTML')

    def add_type(self):
        self.find_element(self.process_type_add_loc).click()

    def send_type_name(self, text):
        self.send_keys(self.type_name_loc, text)

    def type_valid(self):
        self.find_element(self.type_valid_input_loc).click()
        self.find_element(self.type_valid_loc).click()

    def type_invalid(self):
        self.find_element(self.type_valid_input_loc).click()
        self.find_element(self.type_invalid_loc).click()

    def type_submit(self):
        self.find_element(self.type_sumbit_loc).click()

    # 编辑类型
    def edit_type(self ,text):

        title = "[title='" + text + "'] [data-icon='edit']"
        self.driver.find_element_by_css_selector(title).click()

    # 检查提交按钮
    def is_disabled_type_sumbit(self):
        return self.find_element(self.type_sumbit_loc).get_attribute('disabled')

    def type_search(self, text):
        self.send_keys(self.process_type_search_loc, text)

    # 点击搜索到的流程业务类型
    def type_search_click(self, text):
        title = "[title='" + text + "']"
        # print(title)
        self.driver.find_element_by_css_selector(title).click()

    # 关闭业务流程类型 close_type_loc
    def close_type(self):
        self.find_element(self.close_type_loc).click()

    # 右侧流程为空的描述
    def get_process_empty(self):
        return self.find_element(self.process_empty_loc).text

    # 添加新流程
    def add(self):
        self.clickButton(self.addbtn_loc)

    def search(self, text):
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    def search_click(self):
        self.find_elements(self.process_tr_loc)[0].click()
        time.sleep(1)

    def clickimport(self):
        self.clickButton(self.import_loc)

    def savereturn(self):
        self.clickButton(self.SaveReturn_loc)

    def is_disabled_save_return(self):
        return self.find_element(self.SaveReturn_loc).get_attribute('disabled')

    def send_name(self, text):
        self.send_keys(self.process_name_loc, text)
        time.sleep(3)

    def send_describe(self, text):
        self.send_keys(self.describe_loc, text)

    # 保存
    def save(self):
        self.clickButton(self.Save_loc)

    def is_disabled_sava(self):
        return self.find_element(self.Save_loc).get_attribute('disabled')

    # 返回列表
    def backlist(self):
        self.clickButton(self.goBack_loc)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    def close_edit_tab(self):
        '''
         关闭编辑tab
        '''
        self.clickButton(self.closetab_loc)
        time.sleep(1)

    def gettabblelist(self):
        return self.find_elements(self.table_body_list_loc)

    # 去业务类型名称、流程名称错误提示
    def get_type_name_error(self):
        return self.find_element(self.type_name_errorServeMessage_loc).text

    def get_name_error(self):
        return self.find_element(self.name_errorServeMessage_loc).text

    def add_node(self):
        self.find_element(self.add_link_opration_button_loc).click()
        time.sleep(1)

    def get_node_num(self):
        return len(self.find_elements(self.first_node_loc))


    # 流程节点添加
    def click_canvas(self, x, y):
        # canvas_loc
        # ActionChains(self.driver).move_by_offset(x, y).click().perform()
        # ActionChains(self.canvas_loc).move_by_offset(x, y).click().perform()

        ActionChains(self.driver).move_to_element(self.find_elements(self.first_node_loc)[1]).\
            move_by_offset(x, y).click().perform()

    def line_click(self, num):
        self.find_elements(self.line_loc)[num].click()

    def delete_line(self):
        self.find_element(self.delete_line_loc).click()

    # 删除确认
    def comfire_delete(self):
        # self.clickButton(self.comfire_detele_loc)
        self.find_element(self.comfire_detele_loc).click()

    def chose_status(self, text='激活'):
        self.find_elements(self.input_loc)[2].click()
        if text == '非活动的':
            self.find_elements(self.process_status_loc)[1].click()
        elif text == '消退':
            self.find_elements(self.process_status_loc)[2].click()
        else:
            self.find_elements(self.process_status_loc)[0].click()





