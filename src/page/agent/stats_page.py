"""
@author: DT_testing
@file:   stats_page.py
@desc:  【统计管理】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base
from selenium.webdriver.common.keys import Keys


class StatsPage(Base):

    # addbtn_loc = (By.CSS_SELECTOR, '.stats-overview .anticon-plus')

    addbtn_loc = (By.XPATH, '//*[@id="newHeight"]/div/nz-spin/div/div/app-stats/nz-spin/div/div/div[1]/button[1]')
    search_loc = (By.ID, 'Search-input')
    table_head_loc = (By.CSS_SELECTOR, 'thead th')
    table_body_loc = (By.CSS_SELECTOR, 'tbody td.ant-table-cell-fix-left-last')
    list_run_loc = (By.ID, 'run')
    list_Export_loc = (By.ID, 'Export')
    Delete_loc = (By.ID, 'Delete')
    detele_comfirm_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-btns button:nth-child(2)')
    # 返回列表
    backlist_loc = (By.CSS_SELECTOR, '.flex-justify-center button.ant-btn:nth-child(2)')

    # ---添加页面--
    # -标题	id	Title
    title_loc = (By.ID, 'Title')
    # 描述
    # 统计类型	id	StatisticPreselection
    Statis_type_loc = (By.ID, 'StatisticPreselection')
    # 对象权限	id	ObjectModule
    Statis_Object_loc = (By.ID, 'ObjectModule')
    # 权限	id	Permission
    Permission_loc = (By.ID, 'Permission')
    Permissioncheckbox_loc = (By.CSS_SELECTOR, '.ant-select-tree-checkbox-inner')
    # 结果格式	id	Format
    Format_loc = (By.ID, 'Format')
    # 时区	id	TimeZone
    # 创建汇总行	id	SumRow
    SumRow_loc = (By.ID, 'SumRow')
    # 创建汇总列	id	SumCol
    SumCol_loc = (By.ID, 'SumCol')
    # 有效性	id	Valid
    Validinput_loc = (By.ID, 'Valid')
    Valid_loc = (By.CSS_SELECTOR, 'testvalue="是"')
    inValid_loc = (By.CSS_SELECTOR, 'testvalue="否"')

    # 提交	id	baseSubmit
    baseSubmit_loc = (By.ID, 'baseSubmit')
    # 提交并完成	id	baseSubmitList
    baseSubmitList_loc = (By.ID, 'baseSubmitList')
    # 返回列表	id	baseCancel
    baseCancel_loc = (By.ID, 'baseCancel')

    # 01选择全部
    chooseallbtn_loc = (By.ID, 'Select')

    # 02清除所有
    chooseclearbtn_loc = (By.ID, 'Clear')

    # 03反选
    chooseReversebtn_loc = (By.ID, 'Reverse')
    # 04查看选中

    # 05确定
    clickclosebtn_loc = (By.ID, 'closeOption')

    # x、y、过滤器  X-axis
    x_axis_loc = (By.ID, 'previewXAxis')
    y_axis_loc = (By.ID, 'previewYAxis')
    filter_loc = (By.ID, 'previewRestrictions')
    # 点击保存
    closeSumit_loc = (By.ID,'closePreviewModalSumit')
    addx_loc = (By.CSS_SELECTOR, '.ant-modal-content .ant-form-item-control-input')

    # 立即运行  run immediately
    #
    run_immediately_loc = (By.XPATH,
                           '//*[@id="newHeight"]/div/nz-spin/div/div/app-stats-run/nz-spin/div/div/div[2]/form/div[5]/button[1]')
    # run_immediately_loc = (By.CSS_SELECTOR, '.flex-end button:nth-child(1)')
    # 关闭运行
    closerun_loc = (By.CSS_SELECTOR,'.chart-close.text-title')

    # 运行页面的返回列表 .flex-end button:nth-child(2)
    run_backlist_loc = (By.CSS_SELECTOR,'.flex-end button:nth-child(2)')

    vaildtab_loc = (By.ID, 'valid')

    def addstats(self):
        # self.find_element(self.addbtn_loc).click()
        self.clickButton(self.addbtn_loc)

    # 右侧搜索
    def search(self, text):
        self.send_keys(self.search_loc, text)
        time.sleep(1)

    # 点击搜索结果
    def search_result(self):
        self.find_elements(self.table_body_loc)[0].click()
        time.sleep(1)

    def listrun(self):
        self.find_element(self.list_run_loc).click()

    def listexport(self):
        self.find_element(self.list_Export_loc).click()

    def delete(self):
        self.find_element(self.Delete_loc).click()

    def detele_comfirm(self):
        self.clickButton(self.detele_comfirm_loc)

    # 添加页面，输入标题
    def title(self, text):
        self.send_keys(self.title_loc, text)

    # 选择统计类型
    def chosetype(self, text):
        self.find_element(self.Statis_type_loc).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('[testvalue="' + text + '"]').click()

    # 选择对象类型
    def choseobject(self, text):
        self.find_element(self.Statis_Object_loc).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('[testvalue="' + text + '"]').click()

    # 选择权限
    def chosePermission(self, role):
        '''
           选择权限选择第一个
        '''
        self.driver.find_element(*self.Permission_loc).click()
        # self.clickButton(self.Permission_loc)
        time.sleep(0.5)
        ActionChains(self.driver).send_keys(role).perform()
        self.find_elements(self.Permissioncheckbox_loc)[0].click()
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(self.find_element(
            self.Permission_loc)).send_keys(Keys.ESCAPE).perform()
    # 选择结果格式
    def choseFormat(self, format):

        self.driver.find_element(*self.Format_loc).click()
        time.sleep(0.5)
        ActionChains(self.driver).send_keys(format).perform()
        time.sleep(0.5)


    def clickallbtn(self):
        self.driver.find_element(*self.chooseallbtn_loc).click()

    # 点击下拉选之后“确定”按钮
    def clickclosebtn(self):
        self.driver.find_element(*self.clickclosebtn_loc).click()

    # 点击提交
    def submit(self):
        self.find_element(self.baseSubmit_loc).click()

    # 提交并完成
    def submitlist(self):
        self.find_element(self.baseSubmitList_loc).click()

    # 返回列表
    def backlist(self):
        self.find_element(self.baseCancel_loc).click()

    # 点击x 轴
    def clickx(self):
        self.find_element(self.x_axis_loc).click()

    # 点击x轴的保存  closePreviewModalSumit
    def closeSumit(self):
        self.find_element(self.closeSumit_loc).click()

    # x轴选择字段
    def chosex_field(self, text):
        # self.find_element(self.addx_loc).click()
        self.driver.find_element(*self.addx_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        # 选择排在第一位的元素
        self.driver.find_element_by_css_selector('.cdk-virtual-scroll-viewport nz-option-item:nth-child(1)').click()

    # 工单清单时，选择x轴打印的字段
    def chosex_printfield(self, text):
        self.driver.find_element(*self.addx_loc).click()
        # self.driver.find_element(self.addx_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(3)
        self.driver.find_element(*self.chooseallbtn_loc).click()
        self.driver.find_element(*self.clickclosebtn_loc).click()

    # x选择字段值
    def chosex_field_value(self):
        self.find_elements(self.addx_loc)[0].click()
        self.driver.find_element(*self.chooseallbtn_loc).click()
        self.driver.find_element(*self.clickclosebtn_loc).click()

    # 立即运行
    def run_immediately(self):
        self.driver.find_element(*self.run_immediately_loc).click()

    # 关闭运行
    def closerun(self):
        self.driver.find_element(*self.closerun_loc).click()

    # 运行页面的返回列表  run_backlist_loc
    def run_backlist(self):
        self.driver.find_element(*self.run_backlist_loc).click()
        time.sleep(3)

    # 取tab的描述加数量
    def get_total(self):
        return self.find_element(self.vaildtab_loc).text






