"""
@author: DT_testing
@file:   mailmanagement_page.py
@desc:  【邮箱】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class MmailmanagementPage(Base):
    # 发件服务器
    add_loc = (By.CSS_SELECTOR, '[class="admin-ticket-template-btn ant-btn"]')
    add_SendHost_loc = (By.XPATH,
                        '//*[@id="newHeight"]/div/nz-spin/div/div/app-admin-system-mail-list/nz-spin/div/div/div[1]/'
                        'nz-collapse/nz-collapse-panel/div[2]/div/div/button')
    # 发件邮箱  Realname
    add_Sendmail_loc = (By.XPATH,
                        '//*[@id="newHeight"]/div/nz-spin/div/div/app-admin-system-mail-list/nz-spin/div/div'
                        '/div[2]/nz-collapse/nz-collapse-panel/div[2]/div/div/button')
    # 收件服务器地址  ReceiveHost
    add_ReceiveHost_loc = (By.XPATH,
                           '//*[@id="newHeight"]/div/nz-spin/div/div/app-admin-system-mail-list/nz-spin/div/div/div[3]/'
                           'nz-collapse/nz-collapse-panel/div[2]/div/div/button')

    backlist1_loc = (By.CSS_SELECTOR, '.submit-btn button:nth-child(2)')

    backlist2_loc = (By.CSS_SELECTOR, '.ant-modal-close-x')

    # 添加页面的页面，页内块
    page_tab_loc = (By.CSS_SELECTOR, '[role="tab"]')

    def add_SendHost(self):
        # self.find_element(self.add_loc)[0].click()
        self.clickButton(self.add_SendHost_loc)
        # self.find_element(self.add_SendHost_loc).click()

    def add_Sendmail(self):
        # self.find_element(self.add_loc)[1].click()
        self.find_element(self.add_Sendmail_loc).click()

    def add_ReceiveHost(self):
        # self.find_element(self.add_loc)[2].click()
        self.find_element(self.add_ReceiveHost_loc).click()

    # 发件服务器、收件服务器添加页面返回
    def backlist1(self):
        self.find_element(self.backlist1_loc).click()

    def check_backlist1(self):
        self.find_element(self.backlist1_loc)

    # 发件邮箱-返回
    def backlist2(self):
        self.find_element(self.backlist2_loc).click()

    def open_second_tab(self):
        # page_tab_loc
        self.find_elements(self.page_tab_loc)[1].click()
        time.sleep(5)
