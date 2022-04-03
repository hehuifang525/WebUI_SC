"""
@author: DT_testing
@file:   content_template_page.py
@desc:  【内容模板】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base
from selenium.webdriver.common.keys import Keys


class ContentTemplatePage(Base):

    add_btn_loc = (By.CSS_SELECTOR, 'button[class="ant-btn ant-btn-primary"]:nth-child(1)')
    temp_to_role_btn_loc = (By.CSS_SELECTOR, 'button[class="ant-btn ant-btn-primary"]:nth-child(2)')
    search_loc = (By.CSS_SELECTOR, '[placeholder="过滤"]')
    valid_tab_loc = (By.CSS_SELECTOR, '[id="Valid"]')
    invalid_tab_loc = (By.CSS_SELECTOR, '[id="Invalid"]')
    # 删除  Delete
    delete_loc = (By.ID, 'Delete')
    # 删除确认
    confirm_del_loc = (By.CSS_SELECTOR, '.ant-modal-body button:nth-child(2)')

    name_loc = (By.ID, 'Name')
    role_loc = (By.ID, 'Role')
    subject_loc = (By.ID, 'Subject')
    # 内容输入框
    content_loc = (By.CSS_SELECTOR, '[role="textbox"]')
    valid_input_loc = (By.ID, 'ValidID')
    valid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="有效"]')
    invalid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="无效"]')
    comment_loc = (By.ID, 'Comment')

    # 提交、返回列表
    submit_btn_loc = (By.CSS_SELECTOR, '.submit-btn button:nth-child(1)')
    return_list_bth_loc =(By.CSS_SELECTOR, '.submit-btn button:nth-child(2)')

    # 暂无数据
    empty_loc = (By.CSS_SELECTOR, '.ant-empty p')

    def get_empty(self):
        return self.find_element(self.empty_loc).text

    def add(self):
        self.find_element(self.add_btn_loc).click()

    def search(self, search_text):
        self.send_keys(self.search_loc, search_text)

    def delete(self):
        self.find_element(self.delete_loc).click()

        # 确认删除模板

    def confirm_del_model(self):
        self.find_element(self.confirm_del_loc).click()
        time.sleep(2)

    def valid_tab_click(self):
        self.find_element(self.valid_tab_loc).click()

    def invalid_tab_click(self):
        self.find_element(self.invalid_tab_loc).click()

    # 模板-角色
    def temp_to_role(self):
        self.find_element(self.temp_to_role_btn_loc).click()

    # ---start 添加页面
    def name_in(self, name_text):
        self.send_keys(self.name_loc, name_text)

    def subject_in(self, subject_text):
        self.send_keys(self.subject_loc, subject_text)

    def comment(self, comment):
        self.send_keys(self.comment_loc, comment)

    def submit(self):
        self.find_element(self.submit_btn_loc).click()

    def return_list(self):
        self.find_element(self.return_list_bth_loc).click()

    # 输入内容
    def content_in(self, content):
        self.send_keys(self.content_loc, content)

    # 选择角色
    def role(self, role):
        self.find_element(self.role_loc).click()
        ActionChains(self.driver).send_keys(role).perform()
        elem = '[title = "'+role +'"]'
        elem_loc = (By.CSS_SELECTOR, elem)
        self.find_element(elem_loc).click()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # 选择有效，无效
    def valid(self):
        self.find_element(self.valid_input_loc).click()
        self.find_element(self.valid_loc).click()

    def invalid(self):
        self.find_element(self.valid_input_loc).click()
        self.find_element(self.invalid_loc).click()

    # 取名称、所属角色、主题、内容框、有效性、备注的值
    # 正常获取
    def get_name(self):
        return self.find_element(self.name_loc).get_attribute("value")

    # ok
    def get_role(self):
        # return self.find_element(self.role_loc).get_attribute("content")
        return self.find_element(self.role_loc).text

    def get_subject(self):
        return self.find_element(self.subject_loc).get_attribute("value")

    # 可取值，但是有bug，第一个子取不到
    def get_content(self):
        return self.find_element(self.content_loc).text

    # 正常获取
    def get_valid(self):
        return self.find_element(self.valid_input_loc).text

    def get_comment(self):
        return self.find_element(self.comment_loc).get_attribute("value")

    # ---end 添加页面







