"""
@author: DT_testing
@file:   generic_page.py
@desc:  【自动任务】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base
from selenium.webdriver.common.keys import Keys


class GenericPage(Base):
    # 添加按钮
    addbtn_loc = (By.CSS_SELECTOR, '[class="flex-start margin-T15 margin-B10"] button:nth-child(1)')
    exporttall_loc = (By.CSS_SELECTOR, '[class="flex-start margin-T15 margin-B10"] button:nth-child(2)')
    import_loc = (By.CSS_SELECTOR, '[class="flex-start margin-T15 margin-B10"] button:nth-child(3)')
    search_loc = (By.ID, 'Search-input')

    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    # 表头
    table_head_loc = (By.CSS_SELECTOR, '.ant-table-thead th')

    # 运行 复制  删除
    run_loc = (By.ID, 'run')
    copy_loc = (By.ID, 'Copy')
    delete_loc = (By.ID, 'Delete')
    export_loc = (By.ID, 'Export')

    # 删除弹框的确认、取消
    delete_cancel_loc = (By.CSS_SELECTOR, '.ant-modal-body button:nth-child(1)')
    delete_confirm_loc = (By.CSS_SELECTOR, '.ant-modal-body button:nth-child(2)')

    # 无数据
    empty_loc = (By.CSS_SELECTOR,'.ant-empty p')
    # 有效tab、无效tab
    valid_tab_loc = (By.ID, 'valid')
    invalid_tab_loc = (By.ID, 'invalid')

    # 添加页面
    name_loc = (By.ID, 'Name')
    name_errorMessage_loc = (By.ID, 'Name_errorServeMessage')
    # 提交
    submit_loc = (By.CSS_SELECTOR, '.submit-btn .flex-end .ant-form-item.ant-row:nth-child(1) button')
    # 再添加一条
    addmore_loc =(By.CSS_SELECTOR, '.submit-btn .flex-end .ant-form-item.ant-row:nth-child(2) button')
    # 返回列表
    backlist_loc =(By.CSS_SELECTOR, '.submit-btn .flex-end .ant-form-item.ant-row:nth-child(3) button')

    # 导入页面的返回 GoBack
    importback_loc = (By.ID, 'GoBack')

    # 表单中有效性字段
    Valid_input = (By.ID,'ValidID')
    # 0817修改
    # Valid = (By.CSS_SELECTOR, '[testvalue="有效"]')
    # inValid = (By.CSS_SELECTOR, '[testvalue="无效"]')
    Valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(2)')
    inValid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(1)')

    # 增加工单搜索条件
    FilterCondition_loc = (By.ID, 'FilterCondition')
    # 选择第一个搜索字段
    firstCondition_loc = (By.CSS_SELECTOR, '[class="ant-select-item-option-content"]')
    # 优先级
    priority_loc = (By.CSS_SELECTOR, '[title="优先级"]')
    # 选择的条件字段：主题、角色、优先级
    Condition_Subject_loc = (By.ID, 'MIMEBase_Subject')
    Condition_Priority_loc = (By.ID, 'PriorityIDs')
    Condition_Queue_loc = (By.ID, 'QueueIDs')
    # 条件的删除图标
    delete_Condition_Priority_loc = (By.ID, 'PriorityIDs_icon')
    delete_Condition_Subject_loc = (By.ID, 'MIMEBase_Subject_icon')
    delete_Condition_Queue_loc = (By.ID, 'QueueIDs_icon')
    # 01选择全部
    chooseallbtn_loc = (By.ID, 'Select')
    # 02清除所有
    chooseclearbtn_loc = (By.ID, 'Clear')
    # 03反选
    chooseReversebtn_loc = (By.ID, 'Reverse')
    # 04查看选中
    # 05确定
    clickclosebtn_loc = (By.ID, 'closeOption')

    # 选择命中的高亮
    highlight_loc = (By.CSS_SELECTOR, '.font-highlight')

    # 选择更新字段
    updatefield_loc = (By.ID, 'GenericNewAttribute')
    # 更新字段：设置新主题、新的角色、新的优先级
    new_Subject_loc = (By.ID, 'Title')
    new_queue_loc = (By.ID,  'NewQueueID')
    new_priority_loc = (By.ID,  'NewPriorityID')

    # 删除更新的标题、角色、优先级  Title_icon
    delete_new_Priority_loc = (By.ID, 'NewPriorityID_icon')
    delete_new_Subject_loc = (By.ID, 'Title_icon')
    delete_new_Queue_loc = (By.ID, 'NewQueueID_icon')
    add_tab_loc = (By.CSS_SELECTOR, '[role="tab"]')

    # 发件人 主题  内容
    new_note_from_loc = (By.ID, 'NewNoteFrom')
    new_note_subject_loc = (By.ID, 'NewNoteSubject')
    # 2021-12-20调整
    content_loc = (By.CSS_SELECTOR, 'textarea.ant-input')

    # 命令
    new_cmd_loc = (By.ID, 'NewCMD')
    new_module_loc = (By.ID, 'NewModule')

    # 计划的天、小时、分钟
    generic_schedule_loc = (By.CSS_SELECTOR, '[class="generic-schedule-input"]')

    generic_schedule_option_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-viewport nz-option-item')
    # 删除计划的天、小时、分钟
    deletc_generic_schedule_loc = (By.CSS_SELECTOR, '.generic-schedule-input .ant-select-clear')
    # 任务类型
    event_execution_loc = (By.CSS_SELECTOR, '.ant-radio-group label:nth-child(2)')
    # 事件触发器
    eventValues_loc = (By.ID, 'EventValues')
    # 删除事件
    delete_eventValues_loc = (By.CSS_SELECTOR, '#EventValues .ant-select-clear .ant-select-close-icon')

    #-- 执行定制模块--
    # 添加值
    add_parameter_loc = (By.CSS_SELECTOR,'[class="anticon anticon-plus"]')
    # 模块参数键
    parameter_key_loc = (By.CSS_SELECTOR, '[placeholder="键"]')
    # 模块参数值
    parameter_value_loc = (By.CSS_SELECTOR, '[placeholder="值"]')
    # 删除模块参数
    delete_parameter_loc = (By.CSS_SELECTOR, '[class="ng-fa-icon flexible-icon cursor"]')
    # 参数总数
    count_parameter_loc = (By.CSS_SELECTOR, 'nz-tag.ant-tag-blue')




    #   取添加页面的tab:任务设置、选择工单、更新/添加工单属性等
    def get_add_tab(self):
        return self.find_elements(self.add_tab_loc)

    def get_table_head(self):
        return self.find_elements(self.table_head_loc)

    def add(self):
        self.clickButton(self.addbtn_loc)

    def search(self, text):
        self.clickButton(self.search_loc)
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    def clickimport(self):
        self.clickButton(self.import_loc)

    # 点击复制
    def copy(self):
        self.clickButton(self.copy_loc)

    # 运行
    def runclick(self):
        self.clickButton(self.run_loc)

    def checkrun(self):
        self.find_element(self.run_loc)

    def checkcopy(self):
        self.find_element(self.copy_loc)

    def checkdelete(self):
        self.find_element(self.delete_loc)

    def checkexport(self):
        self.find_element(self.export_loc)

    def inputname(self, text):
        self.send_keys(self.name_loc, text)

    def sumbit(self):
        self.clickButton(self.submit_loc)
        time.sleep(2)

    # 再来一条
    def addmore(self):
        self.find_element(self.addmore_loc).click()

    # 取提交按钮的可点击操作  disabled
    def sumbit_disabled(self):
        return self.find_element(self.submit_loc).get_attribute("disabled")

    def addmore_disabled(self):
        return self.find_element(self.submit_loc).get_attribute("disabled")

    # 再添加一条
    def addmore(self):
        self.clickButton(self.addmore_loc)

    # 返回列表
    def backlist(self):
        self.clickButton(self.backlist_loc)
        time.sleep(2)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(4)

    def importback(self):
        self.clickButton(self.importback_loc)
        time.sleep(2)

    # 取名称字段值
    def get_name(self):
        return self.find_element(self.name_loc).get_attribute("value")

    def name_error_message(self):
        return self.find_element(self.name_errorMessage_loc).text

    # 点击删除按钮
    def delete(self):
        self.find_element(self.delete_loc).click()

    # 删除确认、取消
    def delete_cancel(self):
        self.find_element(self.delete_cancel_loc).click()
        time.sleep(1)

    def delete_confirm(self):
        self.find_element(self.delete_confirm_loc).click()
        time.sleep(2)

    def get_empty(self):
        return self.find_element(self.empty_loc).text

    # 切换有效无效tab
    def valid_tab(self):
        self.find_element(self.valid_tab_loc).click()

    def invalid_tab(self):
        self.find_element(self.invalid_tab_loc).click()

    # 有效性选择有效、无效
    def valid(self):
        self.find_element(self.Valid_input).click()
        time.sleep(0.5)
        self.find_element(self.Valid_loc).click()

    def invalid(self):
        self.find_element(self.Valid_input).click()
        time.sleep(0.5)
        self.find_element(self.inValid_loc).click()

    # 选择工单-增加工单搜索条件
    def chose_tickect_fidld(self, text):
        self.driver.find_element(*self.FilterCondition_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        title = '.cdk-virtual-scroll-content-wrapper [title="' + text + '"]'
        # print(title)
        elm_loc = (By.CSS_SELECTOR, title)
        self.find_element(elm_loc).click()

    # 选择工单搜索条件-选择优先级字段
    def chose_tickect_priority(self, text):
        self.driver.find_element(*self.FilterCondition_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.find_element(self.priority_loc).click()


    # 取主题、角色、优先级字段
    def input_condition_subject(self, text):
        self.send_keys(self.Condition_Subject_loc, text)

    def chose_queue(self, text):
        self.driver.find_element(*self.Condition_Queue_loc).click()
        time.sleep(3)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.find_elements(self.highlight_loc)[0].click()
        ActionChains(self.driver).move_to_element(self.find_element(
            self.Condition_Queue_loc)).send_keys(Keys.ESCAPE).perform()

    def chose_priority(self, text):
        # self.driver.find_element(*self.Condition_Priority_loc).click()
        self.find_element(self.Condition_Priority_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        # 选中结果项
        self.driver.find_element(*self.chooseallbtn_loc).click()
        # 点击关闭
        self.driver.find_element(*self.clickclosebtn_loc).click()

    # 取值，取主题值，角色值、优先级值断言
    def get_condition_subject(self):
        return self.find_element(self.Condition_Subject_loc).get_attribute("value")

    def get_condition_queue(self):
        return self.find_element(self.Condition_Queue_loc).text

    def get_condition_priority(self):
        return self.find_element(self.Condition_Priority_loc).text

    # 删除 角色、优先级 条件
    def delete_condition_queue(self):
        self.find_element(self.delete_Condition_Queue_loc).click()

    def delete_condition_priority(self):
        self.find_element(self.delete_Condition_Priority_loc).click()

    # 选择更新的字段值
    def chose_update_fidld(self, field):
        self.find_element(self.updatefield_loc).click()
        # self.driver.find_element(*self.updatefield_loc).click()
        # time.sleep(2)
        ActionChains(self.driver).send_keys(field).perform()  # 搜索使用
        self.find_elements(self.firstCondition_loc)[0].click()
        # time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.find_element(
        #     self.wtlx_loc)).send_keys(Keys.ESCAPE).perform()

    # 设置新的标题、角色、优先级
    def update_title(self,text):
        self.send_keys(self.new_Subject_loc, text)

    def update_queue(self, text):
        self.driver.find_element(*self.new_queue_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.find_elements(self.highlight_loc)[0].click()
        # ActionChains(self.driver).move_to_element(self.find_element(
        #     self.Condition_Queue_loc)).send_keys(Keys.ESCAPE).perform()

    def update_priority(self, text):
        self.driver.find_element(*self.new_priority_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        # self.find_elements(self.firstCondition_loc)[0].click()
        title = 'nz-option-item [title="' + text + '"]'
        # print(title)
        elm_loc = (By.CSS_SELECTOR, title)
        self.find_element(elm_loc).click()
        # # 输入esc收起下拉
        # ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


    # 取更新、添加工单属性的字段值（标题、角色、优先级）
    def get_new_subject(self):
        return self.find_element(self.new_Subject_loc).get_attribute("value")

    def get_new_queue(self):
        return self.find_element(self.new_queue_loc).text

    def get_new_priority(self):
        return self.find_element(self.new_priority_loc).text
        # return self.find_element(self.new_priority_loc).get_attribute("content")
        # return self.find_element(self.new_priority_loc).get_attribute("value")

        # 删除 角色、优先级 条件

    def delete_new_queue(self):
        self.find_element(self.delete_new_Queue_loc).click()

    def delete_new_priority(self):
        self.find_element(self.delete_new_Priority_loc).click()

    def new_note_from(self, text):
        self.send_keys(self.new_note_from_loc, text)

    def clear_new_note_from(self):
        # userName.send_keys(Keys.BACKSPACE)
        ele = self.find_element(self.new_note_from_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

    def new_note_subject(self, text):

        self.send_keys(self.new_note_subject_loc, text)

    def clear_new_note_subject(self):

        ele = self.find_element(self.new_note_subject_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

        # ActionChains(self.driver).send_keys(Keys.CONTROL + 'a').send_keys(Keys.BACKSPACE).perform()

    def send_content(self, text):
        self.send_keys(self.content_loc, text)

    def clear_content(self):
        ele = self.find_element(self.content_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

        # ActionChains(self.driver).send_keys(Keys.CONTROL + 'a').send_keys(Keys.BACKSPACE).perform()

    def new_cmd(self, text):
        self.send_keys(self.new_cmd_loc, text)

    def clear_new_cmd(self):
        ele = self.find_element(self.new_cmd_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

        # ActionChains(self.driver).send_keys(Keys.CONTROL + 'a').send_keys(Keys.BACKSPACE).perform()

    def new_module(self, text):
        self.send_keys(self.new_module_loc, text)

    def clear_new_module(self):
        ele = self.find_element(self.new_module_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

    def get_new_note_from(self):
        return self.find_element(self.new_note_from_loc).get_attribute('value')

    def get_new_note_subject(self):
        return self.find_element(self.new_note_subject_loc).get_attribute('value')

    def get_content(self):
        return self.find_element(self.content_loc).get_attribute('value')

    def get_new_cmd(self):
        return self.find_element(self.new_cmd_loc).get_attribute('value')

    def get_new_module(self):
        return self.find_element(self.new_module_loc).get_attribute('value')

    # 基于时间执行，点击计划的天等并选择值
    def generic_schedule(self, num):
        self.find_elements(self.generic_schedule_loc)[num].click()
        # ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def generic_schedule_option(self, num):
        self.find_elements(self.generic_schedule_option_loc)[num].click()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # 取基于时间执行设置的值
    def get_generic_schedule(self, num):
        return self.find_elements(self.generic_schedule_loc)[num].text

    # deletc_generic_schedule_loc
    def delete_generic_schedule(self,denum, num):
        ele = self.find_elements(self.generic_schedule_loc)[denum]
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_elements(self.deletc_generic_schedule_loc)[num].click()

    # 点击基于事件执行
    def event_execution(self):
        self.find_element(self.event_execution_loc).click()

    # 选择执行的事件e
    def event_values(self, event):
        self.driver.find_element(*self.eventValues_loc).click()
        ActionChains(self.driver).send_keys(event).perform()  # 搜索使用
        time.sleep(1)
        # 选中结果项
        self.driver.find_element(*self.chooseallbtn_loc).click()
        # 点击关闭
        self.driver.find_element(*self.clickclosebtn_loc).click()

    def get_event_values(self):
        time.sleep(5)
        # print(self.find_element(self.eventValues_loc).is_displayed(), '检查元素是否隐藏')
        return self.find_element(self.eventValues_loc).text

        # return self.find_element(self.eventValues_loc).get_attribute("attributeName")

    def delete_event_values(self):
        ele = self.find_element(self.eventValues_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.find_element(self.delete_eventValues_loc).click()

    def count_parameter(self):
        return self.find_element(self.count_parameter_loc).text

    def add_value(self):
        self.find_element(self.add_parameter_loc).click()

    def send_parameter_key(self, num, text):
        ele = self.find_elements(self.parameter_key_loc)[num]
        ele.send_keys(text)

    def send_parameter_value(self, num, text):
        ele = self.find_elements(self.parameter_value_loc)[num]
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)
        ele.send_keys(text)

    def delete_parameter(self, num):
        self.find_elements(self.delete_parameter_loc)[num].click()

    # 取参数键和值
    def get_parameter_key(self, num):
        return self.find_elements(self.parameter_key_loc)[num].get_attribute("value")

    def get_parameter_value(self, num):
        return self.find_elements(self.parameter_value_loc)[num].get_attribute("value")










