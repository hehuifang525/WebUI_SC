"""
@author: DT_testing
@file:   faq_overview_page.py
@desc:  【知识库概览】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class FaqOverviewPage(Base):
    addfaq_loc = (By.CSS_SELECTOR, '.ant-skeleton-active button ')
    right_search_loc = (By.ID, 'faqSearch')
    left_search_loc = (By.ID, 'Search-tree')

    title_loc = (By.ID, 'Title')
    # 关键字
    Keywords_loc = (By.ID, 'Keywords')
    # 类别 CategoryID
    category_loc = (By.ID, 'CategoryID')
    # 有效时间
    Effective_loc = (By.ID, 'Effective')
    # 置顶
    top_loc = (By.ID, 'Top')
    # 状态
    State_loc = (By.ID, 'StateID')
    # 有效性
    validinput_loc = (By.ID, 'ValidID')
    valid_loc = (By.CSS_SELECTOR, '[testvalue="有效"]')
    invalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    context_loc = (By.CSS_SELECTOR, '[role="textbox"]')
    submit_loc = (By.ID, 'submit')
    goBack1_loc = (By.ID, 'goBack')
    # 详情页面内的编辑
    # edit_loc = (By.CSS_SELECTOR,'span.faq-edit-icon')
    edit_loc = (By.CSS_SELECTOR, '.listDetail-info>button')
    # 编辑页面的左上标题
    name_loc= (By.CSS_SELECTOR, 'div.overflow-ellipsis')

    def add(self):
        self.find_element(self.addfaq_loc).click()
        time.sleep(1)

    def inputtitle(self, text):
        self.send_keys(self.title_loc, text)

    def category(self, text):
        title1 =  '[title="' + text + '"]'
        self.driver.find_element(*self.category_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()  # 搜索使用
        self.driver.find_element_by_css_selector(title1).click()

    def send_context(self, text):
        self.send_keys(self.context_loc, text)

    def submit(self):
        self.find_element(self.submit_loc).click()

    def edit(self):
        self.find_element(self.edit_loc).click()

    def gettitle(self):
        return self.find_element(self.title_loc).get_attribute("testvalue")




