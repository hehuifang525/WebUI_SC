"""
@author: DT_testing
@file:   user_search_page.py
@desc:  【工单搜索】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class UserSearchPage(Base):

    full_text_loc = (By.CSS_SELECTOR, ".dynamic-fields .ant-spin-container>form>div:nth-child(1) input")
    # 优先级，在第二个
    # priority_option_loc = (By.CSS_SELECTOR, ".dynamic-fields .ant-spin-container>form>div:nth-child(2) input")
    # 搜索条件
    search_condition_input_loc = (By.CSS_SELECTOR, ".dynamic-fields .ant-spin-container>form>div input")
    search_btn_loc = (By.CSS_SELECTOR, "button.search")

    total_tab_loc = (By.CSS_SELECTOR, '[id="Grand total"]')
    # 无内容
    empty_loc = (By.CSS_SELECTOR, 'p.ant-empty-description')
    # 增加另外一个搜索条件：
    add_another_search_field_loc = (By.ID, 'AddAnotherSearchField')
    # 优先级
    priority_loc = (By.CSS_SELECTOR, '[title="优先级"]')

    # 下拉框中，选择全部、确定
    select_all_loc = (By.ID, 'Select')
    close_optionall_loc = (By.ID, 'closeOption')
    # 表头元素 thead th
    table_th_loc = (By.CSS_SELECTOR, 'thead th')
    table_td_first_loc = (By.CSS_SELECTOR, '#baseTableTbody tr:nth-child(2) td')   # 返回搜索的第一行记录

    # 搜索后第一个的工单号,标题
    number_loc = (By.CSS_SELECTOR, '#baseTableTbody tr:nth-child(2) td:nth-child(2)')
    title_loc = (By.CSS_SELECTOR, '#baseTableTbody tr:nth-child(2) td:nth-child(3)')

    # 工单详情页的工单号
    details_num_loc = (By.CSS_SELECTOR,'[class="flex-start header-info-number"]')
    details_title_loc = (By.CSS_SELECTOR,'span.header-info-text span:nth-child(1)')

    # 提示
    tip_loc = (By.CSS_SELECTOR,'.ant-message-custom-content span')

    # ---模板---
    # 添加模板、保存模板、取消、删除
    add_model_loc = (By.CSS_SELECTOR,'.templat-search-icon i')
    save_model_loc = (By.CSS_SELECTOR, '.flex-start.ticket-search-resultFormat button:nth-child(1)')
    cancel_model_loc = (By.CSS_SELECTOR, '.flex-start.ticket-search-resultFormat button:nth-child(2)')
    delete_model_loc = (By.CSS_SELECTOR, ".cdk-overlay-pane .anticon-close")
    search_model_loc =(By.ID, 'searchtickettemplate')
    model_name_loc = (By.CSS_SELECTOR, '[placeholder="输入模板名称"]')

    # 删除确认
    confirm_del_loc = (By.CSS_SELECTOR, '.ant-modal-body button:nth-child(2)')

    # --右上角搜索模板
    template_search_title_loc = (By.CSS_SELECTOR, 'a.header-template-search-title')
    cursor_tab_loc= (By.CSS_SELECTOR, '.cursor.nav-horizontal-active .anticon.anticon-close')
    total_temp_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-viewport nz-option-item')
    right_up_total_temp_loc = (By.CSS_SELECTOR,'.header-template-search li')

    # 刷新当前tab
    refresh_tab_loc = (By.CSS_SELECTOR, '.nav-horizontal-active .anticon-sync')
    # 展示搜索结果 [type="radio"]
    show_search_results_loc = (By.CSS_SELECTOR, '.ticket-search div label input')
    # show1_search_results_loc= (By.XPATH,'//*[@id="newHeight"]/div/nz-spin/div/div/app-ticket-search/nz-spin/div/div/nz-skeleton/nz-collapse/nz-collapse-panel/div[2]/div/div/div[4]/div/nz-radio-group/label[3]/span[1]/span')
    # 删除搜索条件
    delete_condition_loc = (By.CSS_SELECTOR, '.ticket-search-condition-icon i')
    # 展示的搜索字段名称  .dynamic-fields .flex-align-center label
    dynamic_fields_loc = (By.CSS_SELECTOR, '.dynamic-fields .flex-align-center label')



    def full_text_in(self, full_text):
        self.send_keys(self.full_text_loc, full_text)

    # 点击搜索
    def search_click(self):
        self.find_element(self.search_btn_loc).click()

    # 取搜索的值
    def get_total_tab(self):
        return self.find_element(self.total_tab_loc).get_attribute("title")

    def get_empty_text(self):
        return self.find_element(self.empty_loc).text

    # # 选择优先级作为搜索条件
    # def add_priority(self, text):
    #     self.find_element(self.add_another_search_field_loc).click()
    #     # 输入值
    #     ActionChains(self.driver).send_keys(text).perform()
    #     # 点击
    #     self.find_element(self.priority_loc).click()

    # 选择搜索条件
    def add_condition(self, text):
        self.find_element(self.add_another_search_field_loc).click()
        # 输入值
        ActionChains(self.driver).send_keys(text).perform()
        # 点击
        title = '[title="' + text + '"]'
        title_loc = (By.CSS_SELECTOR, title)
        self.find_element(title_loc).click()

    # 点击第二个搜索字段，这里为优先级
    # def second_option_click(self):
    #     self.find_element(self.priority_option_loc).click()

    def chose_all(self):
        self.find_element(self.select_all_loc).click()
        self.find_element(self.close_optionall_loc).click()

    def close_optionall(self):
        self.find_element(self.close_optionall_loc).click()

    # 取工单号
    def get_number(self):
        return self.find_element(self.number_loc).text

    def get_ticket_title(self):
        return self.find_element(self.title_loc).text

    def get_details_num(self):
        return self.find_element(self.details_num_loc).text

    def get_details_title(self):
        """取工单详情中的标题"""
        return self.find_element(self.details_title_loc).text

    def get_tip(self):
        return self.find_element(self.tip_loc).text

    def add_model(self):
        self.find_element(self.add_model_loc).click()

    def save_model(self):
        self.find_element(self.save_model_loc).click()

    def cancel_model(self):
        self.find_element(self.cancel_model_loc).click()

    def delete_model(self, title):
        # 点击输入框，搜索
        self.find_element(self.search_model_loc).click()
        ActionChains(self.driver).send_keys(title).perform()
        delete_ele = '[title="' + title + '"] .anticon-close'
        title_loc = (By.CSS_SELECTOR, delete_ele)
        self.find_element(title_loc).click()
        time.sleep(1)

    # 确认删除模板
    def confirm_del_model(self):
        self.find_element(self.confirm_del_loc).click()
        time.sleep(2)

    def search_model(self):
        self.find_element(self.search_model_loc).click()

    def input_model_name(self, text):
        self.send_keys(self.model_name_loc, text)

    # 封装一个title作为变量的方法
    def select_by_title(self, title):
        title ='[title="' + title + '"]'
        title_loc = (By.CSS_SELECTOR, title)
        self.find_element(title_loc).click()

    # 右上角选择搜索模板，并点击  Upper right corner
    def upper_right_corner_temp_search(self, temp_name):

        elemt = self.find_element(self.template_search_title_loc)
        ActionChains(self.driver).move_to_element(elemt).perform()

        temp_name_loc = (By.CSS_SELECTOR, 'li[title="' + temp_name + '"]')
        self.find_element(temp_name_loc).click()

    # 鼠标移动到右上角选择搜索模板，
    def move_upper_right(self):
        elemt = self.find_element(self.template_search_title_loc)
        ActionChains(self.driver).move_to_element(elemt).perform()

    # 关闭当前tab
    def close_tab(self):
        self.find_element(self.cursor_tab_loc).click()

    # 刷新当前tab
    def refresh_current_tab(self):
        self.find_element(self.refresh_tab_loc).click()

    # 返回搜索模板下拉的值
    def get_total_temp_loc(self):
        return self.find_elements(self.total_temp_loc)

    # 返回右上角工单搜索模板的下拉值
    def get_right_total_temp_loc(self):
        return self.find_elements(self.right_up_total_temp_loc)

    def show_search_results_click(self, results):
        elm = self.find_elements(self.show_search_results_loc)
        print(len(elm), "元素长度")
        if results == "CSV":
            self.find_elements(self.show_search_results_loc)[1].click()
        elif results == "Excel":
            self.find_elements(self.show_search_results_loc)[2].click()
            # self.find_element(self.show1_search_results_loc).click()

        else:
            self.find_elements(self.show_search_results_loc)[0].click()

    # 删除搜索条件
    def delete_search_condition(self, num):
        self.find_elements(self.delete_condition_loc)[num].click()

    # 点击搜索条件输入框
    def search_condition_input_click(self, num):
        '''
            num:是页面中搜索字段的排序，从0开始
        '''
        self.find_elements(self.search_condition_input_loc)[num].click()

    # 取页面显示的动态字段
    def get_dynamic_fields(self):
        return self.find_elements(self.dynamic_fields_loc)

    def get_table_th(self):
        """
            取搜索结果后的表头元素
        """
        return self.find_elements(self.table_th_loc)

    def get_table_td_first(self):
        """
            取搜索结果后的第一行元素
        """
        return self.find_elements(self.table_td_first_loc)














